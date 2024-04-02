from aiogram import Router, types, F
from aiogram.filters import Command


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[

            [
                types.InlineKeyboardButton(text='наш сайт', url="https://online.geeks.kg/")
            ],

            [
                types.InlineKeyboardButton(text='наш инст', url="https://www.instagram.com/")
            ],

            [
                types.InlineKeyboardButton(text='o nas', callback_data='about us')
            ],

            [
                types.InlineKeyboardButton(text='donate', callback_data='donate us')
            ]

        ]
    )
    return keyboard