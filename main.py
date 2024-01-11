import sys
import asyncio
import logging

from aiogram import Bot,Dispatcher
from core.settings import settings
from core.hanglers.start_hang import keyboard_router,english_router,parse_router,hystory_router
from core.commands.menu_command import menu_command
async def main():
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()
    await menu_command(bot)

    dp.include_router(keyboard_router)
    dp.include_router(english_router)
    dp.include_router(parse_router)
    dp.include_router(hystory_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
