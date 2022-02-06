# -*- coding: utf-8 -*-

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from data.config import *
from data.keyboard import main_inline_keyboard, share_phone_number

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, TEXT, reply_markup=main_inline_keyboard)


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "⁉ Введите /start")


@dp.callback_query_handler(text="yes")
async def yes_function(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "✅ Отлично, осталось только поделится вашим контактом и я в "
                                                  "ближайшее время напишу/позвоню вам!",
                           reply_markup=share_phone_number)


@dp.message_handler(content_types=["contact"])
async def text(message: types.Message):
    phone = message.contact.phone_number
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    await bot.send_message(message.from_user.id, "✅ Замечательно, в ближайшее время я позвоню/напишу вам")
    await bot.send_message("1075498641", f"Получен пользователь: {first_name} {last_name}\nТелефон: {phone}")


@dp.message_handler()
async def wrong_message(message: types.Message):
    await bot.send_message(message.from_user.id, "‼ Ничего вводить не требуется")


if __name__ == "__main__":
    executor.start_polling(dp)
