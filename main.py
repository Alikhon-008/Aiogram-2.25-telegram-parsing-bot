from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from keyboards import *
from texno_pars import texno
from aiogram.types import Message
from configs import get_value

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['location'])
async def send_location(message: Message):
    latitude = 15.32129
    longitude = 66.03343
    await bot.send_location(message.chat.id, latitude, longitude)
    await message.answer("Наш геолокация 📍")


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Привет <b>{full_name}!</b> Добро пожаловать")
    await show_category_news(message)


async def show_category_news(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Выберите Категорию", reply_markup=buttons_category())


@dp.message_handler(content_types=['text'])
async def get_news_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_product = texno(get_value(category_text))

    for product in get_product:
        images = product.get('image')
        title = product.get('title')
        credit_price = product.get('credit_price')
        price = product.get('price')
        link = product.get('link')
        # print(images)

        await message.answer_photo(photo=images, caption=f"""
Имя: {title}

Цена: {price}
Рассрочка: {credit_price}
Подробнее по ссылке: {link}""")


executor.start_polling(dp)
