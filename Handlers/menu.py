from aiogram import Router, F, types
from aiogram.filters import Command


menu_router = Router()


@menu_router.message(Command('menu'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Пиццы'),
                types.KeyboardButton(text='Горячие блюда')
            ],
            [
                types.KeyboardButton(text='Гарниры'),
                types.KeyboardButton(text='Напитки')
            ],
        ], resize_keyboard=True
    )
    await message.answer('Меню:', reply_markup=kb)


@menu_router.message(F.text.lower() == 'пиццы')
async def shop_horror(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Скоро будут добавлены! ', reply_markup=kb)


@menu_router.message(F.text.lower() == 'горячие блюда')
async def shop_horror(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Скоро будут добавлены! ', reply_markup=kb)


@menu_router.message(F.text.lower() == 'гарниры')
async def shop_horror(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Скоро будут добавлены! ', reply_markup=kb)


@menu_router.message(F.text.lower() == 'напитки')
async def shop_horror(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Скоро будут добавлены! ', reply_markup=kb)
