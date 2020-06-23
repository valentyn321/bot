from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from main import bot, dp
from config import admin_id
from keyboards import main_menu, menu_brends

import sqlite3

from lamoda.lamoda_clothes import parse_cl
from lamoda.lamoda_shoes import parse_sh

CONST_OFFSET = 0 

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")
    

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.answer(
        '<strong>Привет!</strong> Погнали за скидками!\nВыберете пункт ниже:', 
        reply_markup=main_menu
    )

@dp.message_handler(Text("Обувь с мультибрендовых сайтов"))
async def multi_shoes(message: Message):
    parse_sh() 
    conn = sqlite3.connect('lamoda/lamoda_shoes.db')
    c = conn.cursor()

    SQL_STRING = 'SELECT * FROM sales ORDER BY random() LIMIT 10'
    c.execute(SQL_STRING)

    items = c.fetchall()

    for item in items:
        title = item[1]
        link = item[2]
        price = item[3]
        await message.answer(f"<strong>Модель:</strong> {title}\n\n<strong>Ссылка:</strong> <em>{link}</em>\n\n<strong>Цена:</strong> {price} UAH") 

@dp.message_handler(Text("Одежда с мультибрендовых сайтов"))
async def multi_clothes(message: Message):
    parse_cl()    
    conn = sqlite3.connect('lamoda/lamoda_clothes.db')
    c = conn.cursor()

    SQL_STRING = 'SELECT * FROM sales ORDER BY random() LIMIT 10'
    c.execute(SQL_STRING)

    items = c.fetchall()

    for item in items:
        title = item[1]
        link = item[2]
        price = item[3]
        await message.answer(f"<strong>Модель:</strong> {title}\n\n<strong>Ссылка:</strong> <em>{link}</em>\n\n<strong>Цена:</strong> {price} UAH") 

@dp.message_handler(Text("Поиск по брендам"))
async def PUMA(message: Message):    
        await message.answer('Выбери один из следующих брэндов:', reply_markup=menu_brends)  


@dp.message_handler(Text("PUMA"))
async def PUMA(message: Message, CONST_OFFSET=CONST_OFFSET):
    conn = sqlite3.connect('/home/valentyn/Documents/projects/shopbot/code/puma/puma_shoes.db')
    c = conn.cursor()

    SQL_STRING = 'SELECT * FROM sales '
    c.execute(SQL_STRING)

    items = c.fetchall()
    if len(items) == 0:
        CONST_OFFSET = 0
    else:
        CONST_OFFSET = CONST_OFFSET + 5  

    for item in items:
        title = item[1]
        link = item[2]
        price = item[3]
        await message.answer(f"<strong>Модель:</strong> {title}\n\n<strong>Ссылка:</strong> <em>{link}</em>\n\n<strong>Цена:</strong> {price}")
  