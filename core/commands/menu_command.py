from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def menu_command(bot:Bot):
    commands = [
        BotCommand(
            command='/start',
            description='Start'
        ),
        BotCommand(
            command='/end',
            description='Menu'
        ),
        BotCommand(
            command='/delete_his',
            description='Delete history'
        )
    ]
    await bot.set_my_commands(commands,BotCommandScopeDefault())