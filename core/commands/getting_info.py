from bs4 import BeautifulSoup
import requests
import aiohttp
import asyncio
from urllib.parse import urljoin,quote
from core.bases.model import Product

async def parser(input_val: str, url: str = "https://www.list.am/category"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    input_val = input_val.replace(" ", "+")
    full_url = urljoin(url, f"?q={input_val}")

    async with aiohttp.ClientSession() as session:
        async with session.get(full_url, headers=headers) as response:
            if response.status != 200:
                return f"There is an error {response.status}"

            html = await response.text()

    soup = BeautifulSoup(html, 'lxml')
    all_a_elem = soup.select('a[href*="/item/"]')

    results = []
    name = ''
    info = ''
    item_id = ''
    link = ''
    for item in all_a_elem:
        name_div = item.find('div').find('div')
        price_div = item.find('div', class_='p')
        info_div = item.find('div', class_='at')
        item_id = item['href'].split('/')[-1]
        link_l = f"https://www.list.am{item['href']}"

        if name_div and price_div and info_div and link_l:
            name = name_div.text.strip()
            price = price_div.text.strip()
            info = info_div.text.strip()
            results.append(Product(
                item_id=item_id,
                name=name,
                price=price,
                additional_info=info,
                link=link_l
            ))

        elif price_div is None:
            results.append(Product(
                item_id=item_id,
                name=name,
                price='',
                additional_info=info,
                link=link_l

            ))
        elif info is None:
            results.append(Product(
                item_id=item_id,
                name=name,
                price=price,
                additional_info='NULL',
                link=link_l
            ))
    return results


def check_status(result):
    for product in result:
        if isinstance(product, Product):
            pass
        else:
            return 0
    return 1



