from aiogram.utils.keyboard import  InlineKeyboardBuilder, InlineKeyboardButton,InlineKeyboardMarkup
import emoji

flag_armenia = "🇦🇲"
flag_great_britain = "🇬🇧"
def lang_choise():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'{flag_great_britain} -> {flag_armenia}',callback_data="mode_en_am")
    builder.button(text=f'{flag_armenia} -> {flag_great_britain}', callback_data="mode_am_en")
    return builder.as_markup()