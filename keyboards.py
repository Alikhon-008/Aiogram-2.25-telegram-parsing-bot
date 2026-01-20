from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from configs import CATEGORIES


def buttons_category():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for category in CATEGORIES.keys():
        btn = KeyboardButton(text=category)
        buttons.append(btn)
    markup.add(*buttons)
    return markup