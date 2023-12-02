from aiogram import Router,F
from aiogram.filters import Command,CommandStart
from aiogram import types
import asyncio
from core.keyboards.key_board import creating_table
from core.keyboards.english_keys import english_table
from core.commands.english_words import tables_names
from core.commands.taking_words import get_word
from core.keyboards.language_choise import lang_choise
from core.keyboards.work_words import next_am_word,next_en_word
keyboard_router = Router()
english_router = Router()

stored_callback_data = {}

@keyboard_router.message(CommandStart())
async def cmd_start(message:types.Message):
    await  message.answer("Hello, You connected to my Bot. To start parsing write /run")

@keyboard_router.message(Command("run"))
async def cmd_keyboard(message:types.Message):
    await message.answer("Choose one of this buttons",reply_markup=creating_table())

@keyboard_router.callback_query(F.data == "parsing_start")
async def send_parse(callback: types.CallbackQuery):
    await callback.message.answer("PARSE")

@keyboard_router.callback_query(F.data == "show_history")
async def send_history(callback: types.CallbackQuery):
    await callback.message.answer("his")

@english_router.callback_query(F.data == "english_vocabulary")
async def send_english(callback: types.CallbackQuery):
    await callback.message.answer(f"Choose the number of page \u2193",reply_markup=english_table())

@english_router.callback_query(lambda query: any(table_name in query.data for table_name in tables_names))
async def getting_words(callback: types.CallbackQuery):
    global stored_callback_data
    stored_callback_data[callback.from_user.id] = [callback.data]
    await callback.message.answer(f"Chose the mode",reply_markup=lang_choise())

@english_router.callback_query(F.data == 'mode_en_am')
async def giving_en_words(callback:types.CallbackQuery):
    global stored_callback_data
    result = get_word(stored_callback_data[callback.from_user.id][0])
    update_val =  stored_callback_data[callback.from_user.id] + result
    stored_callback_data[callback.from_user.id] = update_val
    await callback.message.answer("Write /end to end the process.")
    await callback.message.answer(result[0],reply_markup=next_en_word())


@english_router.callback_query(F.data == 'mode_am_en')
async def giving_am_words(callback:types.CallbackQuery):
    global stored_callback_data
    result = get_word(stored_callback_data[callback.from_user.id][0])
    update_val = stored_callback_data[callback.from_user.id] + result
    stored_callback_data[callback.from_user.id] = update_val
    await callback.message.answer("Write /end to end the process.")
    await callback.message.answer(result[1],reply_markup=next_am_word())

@english_router.callback_query(F.data == "next_am_word")
async def next_word_callback(callback: types.CallbackQuery):
    global stored_callback_data

    result = stored_callback_data[callback.from_user.id][1]
    await callback.message.answer(result)
    await asyncio.sleep(1)
    new_wrd = get_word(stored_callback_data[callback.from_user.id][0])
    stored_callback_data[callback.from_user.id][1] = new_wrd[0]
    stored_callback_data[callback.from_user.id][2] = new_wrd[1]
    await callback.message.answer(new_wrd[1],reply_markup=next_am_word())

@english_router.callback_query(F.data == "next_en_word")
async def next_word_callback(callback: types.CallbackQuery):
    global stored_callback_data

    result = stored_callback_data[callback.from_user.id][2]
    await callback.message.answer(result)
    await asyncio.sleep(1)
    new_wrd = get_word(stored_callback_data[callback.from_user.id][0])
    stored_callback_data[callback.from_user.id][1] = new_wrd[0]
    stored_callback_data[callback.from_user.id][2] = new_wrd[1]
    await callback.message.answer(new_wrd[0], reply_markup=next_en_word())

@english_router.message(Command('end'))
async def returning_to_main(message:types.Message):
    await message.answer("Choose one of this buttons", reply_markup=creating_table())

