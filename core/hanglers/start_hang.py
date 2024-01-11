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
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from core.commands.working_with_hystory import making_hystory,getting_history,delete_names
from core.commands.getting_info import parser,check_status
from core.commands.creating_exel_file import add_sheet_by_id,delete_sheet_by_id,delete_file
import openpyxl
from aiogram.types import FSInputFile
import os

keyboard_router = Router()
english_router = Router()
parse_router = Router()
hystory_router = Router()
stored_callback_data = {}

class Form(StatesGroup):
    user_id = State()
    item_name = State()

@keyboard_router.message(CommandStart())
async def cmd_start(message:types.Message):
    await  message.answer("Hello, You connected to my Bot. To start parsing write /run")

@keyboard_router.message(Command("run"))
async def cmd_keyboard(message:types.Message):
    await message.answer("Choose one of this buttons",reply_markup=creating_table())
    await message.answer("🔎 Choose for parsing information \n"
                         "📜 Choose for seeing your last 5 searches \n"
                         "📚 Choose for practicing your english\n"
                         "🗑 You can delete your search history")

@parse_router.callback_query(F.data == "parsing_start")
async def send_parse(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Write item name for parsing")
    await state.set_state(Form.item_name)

@parse_router.message(Form.item_name)
async def process_item_name(message:types.Message, state : FSMContext):
    await state.update_data(user_id=message.from_user.id)
    data = await state.update_data(item_name=message.text)
    value = data["item_name"]
    id = data["user_id"]
    making_hystory(value,id)
    await state.clear()
    res = await parser(input_val=value)
    status = check_status(res)
    if not status:
        await message.answer(f"There is no item with the name {value}")
    else:
        await add_sheet_by_id(res,message.from_user.id)
        await delete_sheet_by_id(message.from_user.id)
        excel_filename = f'{message.from_user.id}.xlsx'
        file = FSInputFile(excel_filename)
        await message.answer_document(document=file)
        os.remove(f"C:\\Users\\Mikayel\\PycharmProjects\\My-Bots\\{message.from_user.id}.xlsx")

@hystory_router.callback_query(F.data == "show_history")
async def send_history(callback: types.CallbackQuery):
    await callback.message.answer("Your parsing history⬇")
    history = getting_history(callback.from_user.id)
    if history == "**":
        await callback.message.answer("You don't have searches yet!")
    else:
        for item in history.split("|"):
            if item != "":
                await callback.message.answer(item)

@hystory_router.message(F.text == "/delete_his")
async def dt_history(message : types.Message):
    delete_names(message.from_user.id)
    await message.answer("History was deleted🗑")
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

