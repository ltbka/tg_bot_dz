from aiogram import Router, types, F
from aiogram.filters import Command


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[

            [
                types.InlineKeyboardButton(text='Наш сайт', url="https://mypizza.kg/"),
                types.InlineKeyboardButton(text='Инстаграм', url="https://www.instagram.com/mypizzakg/?hl=en")
            ],

            [
                types.InlineKeyboardButton(text='Контакты', callback_data='contacts'),
                types.InlineKeyboardButton(text='Адрес', callback_data='adress')
            ],

            [
                types.InlineKeyboardButton(text='Меню', callback_data='Menu' )
            ]

        ]
    )
    return keyboard

def menu_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Пиццы', callback_data='food'),
                types.InlineKeyboardButton(text='Горячие Блюда', callback_data='food')
            ],

            [
                types.InlineKeyboardButton(text='Гарниры', callback_data='food'),
                types.InlineKeyboardButton(text='Напитки', callback_data='food')
            ]

        ]
    )
    return keyboard
#
#
# def order_kb():
#     kb = types.InlineKeyboardMarkup(
#         inline_keyboard=[
#             [types.InlineKeyboardButton(text='Заказать', callback_data="order_")]
#         ]
#     )

