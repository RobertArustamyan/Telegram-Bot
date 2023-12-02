from aiogram.utils.keyboard import  InlineKeyboardBuilder, InlineKeyboardButton,InlineKeyboardMarkup


def next_am_word():

    builder = InlineKeyboardBuilder()
    builder.button(text='Next',callback_data='next_am_word')
    builder.adjust(1)
    return builder.as_markup()
def next_en_word():

    builder = InlineKeyboardBuilder()
    builder.button(text='Next',callback_data='next_en_word')
    builder.adjust(1)
    return builder.as_markup()