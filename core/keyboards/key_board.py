from aiogram.utils.keyboard import  InlineKeyboardBuilder, InlineKeyboardButton
from aiogram import types

def creating_table():
    builder = InlineKeyboardBuilder()
    builder.add(
            types.InlineKeyboardButton(text="Parsing\U0001F50D", callback_data="parsing_start"),
        )
    builder.add(
        types.InlineKeyboardButton(text="History\U0001F4DC", callback_data="show_history")
    )
    builder.add(
            types.InlineKeyboardButton(text="English\U0001F4DA", callback_data="english_vocabulary")
        )
    return builder.as_markup()