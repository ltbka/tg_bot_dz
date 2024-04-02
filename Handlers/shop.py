from aiogram import Router, F, types
from aiogram.filters import Command


shop_router = Router()


@shop_router.message(Command('shop'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='drama'),
                types.KeyboardButton(text='romantic')
            ],
            [
                types.KeyboardButton(text='xorror'),
                types.KeyboardButton(text='fantastic')
            ],
        ], resize_keyboard=True
    )
    await message.answer('Viberite zhanr', reply_markup=kb)


@shop_router.message(F.text.lower() == 'xorror')
async def shop_horror(message: types.Message):
    # kb = types.ReplyKeyboardRemove() для закрытия, reply_markup=kb
    await message.answer('vse knigi zhanra')
