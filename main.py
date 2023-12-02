import sys
import asyncio
import logging

from aiogram import Bot,Dispatcher
from core.settings import settings
from core.hanglers.start_hang import keyboard_router,english_router
async def main():
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()

    dp.include_router(keyboard_router)
    dp.include_router(english_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
