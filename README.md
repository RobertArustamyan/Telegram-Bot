# Telegram Bot

---

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-<version>-blue.svg)](https://github.com/aiogram/aiogram)
[![Requests](https://img.shields.io/badge/Requests-Latest-blue.svg)](https://pypi.org/project/requests/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-<version>-green.svg)](https://pypi.org/project/beautifulsoup4/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-blue.svg)](https://pandas.pydata.org/)
[![openpyxl](https://img.shields.io/badge/openpyxl-Latest-blue.svg)](https://pypi.org/project/openpyxl/)
[![SQLite](https://img.shields.io/badge/SQLite-Latest-blue.svg)](https://www.sqlite.org/)


This Telegram bot is built using the Aiogram framework in Python. It helps to study English words. It also has a scrapping
abiliti from 'https://www.list.am/' and returns the result as excel file. You can also see the history of searches.

## Prerequisites

Before running the Telegram bot, make sure you have the following prerequisites installed and configured:

- **Python 3.x:** Ensure you have Python 3.x installed on your machine.

- **Required Python packages:** Aiogram, requests, beautifulsoup4, pandas, openpyxl, sqlite3


## Start
After clicking the `START` button or typing `/start`, you will see it.

![start](photoes/start.png)

Then click `/run` to see the menu

## Menu
* Parsing
* History
* Englsih

Every button is responsible for its function

![menu](photoes/menu.png)

## Parsing

After clicking the "Parsing" button, it will prompt the user with the text:
`Write item name for parsing`.The bot will then wait until the user inputs the name of the item.

#### Result

For example, if the user inputs `Iphone`, the bot will return:

![result](photoes/exel.png)

The input `Iphone` will be saved in the parsing history.

## History

History button will return the last 5 items of parsing.

## English

After clicking, the bot will provide 20 buttons corresponding to pages. Each page contains approximately 30-40 words.
And after that, you can choose the mode, and it will give the random word from page.

![english](photoes/english.png)

## Additional Commands

Also, here are additional commands for starting, menu, and deleting history.

![add](photoes/add.png)