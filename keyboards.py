from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Обувь с мультибрендовых сайтов'),
        ],
        [
            KeyboardButton(text='Одежда с мультибрендовых сайтов'),
        ],
        [
            KeyboardButton(text='Обратная связь, поддержка')
        ]
    ],
    resize_keyboard=True
)

menu_brends = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='PUMA'),
        ],
    ],
    resize_keyboard=True
)