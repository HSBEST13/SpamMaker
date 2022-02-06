# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

main_inline_keyboard = InlineKeyboardMarkup().add(
    KeyboardButton(text="😍 Да!", callback_data="yes")
)

share_phone_number = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton(text="📲 Поделится контактом", request_contact=True)
)
