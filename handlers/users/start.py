from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.mainKBS import menu_keyboard_eng, menu_keyboard_esp, menu_keyboard_port
from loader import dp
from states.AllStates import MainStates
from utils.db_api import quick_commands as commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    user_id = message.from_user.id
    referrer = None

    await state.update_data(name=name)
    await state.update_data(id=user_id)
    await state.update_data(referrer=referrer)

    await message.answer(f"Hello, {name}, choose your language", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="English",callback_data="eng_lang"),
                InlineKeyboardButton(text="Español",callback_data="esp_lang"),
                InlineKeyboardButton(text="Português",callback_data="port_lang"),

            ]
        ]
    ))

    await MainStates.lang_choose.set()


@dp.callback_query_handler(text="eng_lang", state=MainStates.lang_choose)
async def bot_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.answer(cache_time=15)

    name = data["name"]
    user_id = data["id"]
    referrer = data["referrer"]

    await call.message.answer(f"Hello, {name}", reply_markup=menu_keyboard_eng)
    await call.message.answer_photo(photo=InputFile("images/random.webp"))
    await state.update_data(menu=menu_keyboard_eng)

    await call.message.delete()

    await commands.add_user(user_id, name, 0, 0, 0, "ENG", referrer, False, "", 0, 0, 0, 0, 0)

    await MainStates.main_menu.set()


@dp.callback_query_handler(text="esp_lang", state=MainStates.lang_choose)
async def bot_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.answer(cache_time=15)

    name = data["name"]
    user_id = data["id"]
    referrer = data["referrer"]

    await call.message.answer(f"Hola, {name}", reply_markup=menu_keyboard_esp)
    await call.message.answer_photo(photo=InputFile("images/random.webp"))
    await state.update_data(menu=menu_keyboard_esp)

    await call.message.delete()

    await commands.add_user(user_id, name, 0, 0, 0, "ESP", referrer, False, "", 0, 0, 0, 0, 0)

    await MainStates.main_menu.set()


@dp.callback_query_handler(text="port_lang", state=MainStates.lang_choose)
async def bot_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.answer(cache_time=15)

    name = data["name"]
    user_id = data["id"]
    referrer = data["referrer"]

    await call.message.answer(f"Olá, {name}", reply_markup=menu_keyboard_port)
    await call.message.answer_photo(photo=InputFile("images/random.webp"))
    await state.update_data(menu=menu_keyboard_port)

    await call.message.delete()

    await commands.add_user(user_id, name, 0, 0, 0, "PORT", referrer, False, "", 0, 0, 0, 0, 0)

    await MainStates.main_menu.set()