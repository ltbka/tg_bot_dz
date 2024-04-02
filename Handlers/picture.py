from aiogram import Router, types
from aiogram.filters import Command
import os
from random import choice
# from random import choice
pic_router = Router()


@pic_router.message(Command('pic'))
async def send_picture(message: types.Message):
    file = types.FSInputFile("D:/pyth/pythonProject25/venv/pictures/images.jpg")
    await message.answer_photo(photo=file, caption='картинка')


@pic_router.message(Command('random_pic'))
async def send_picture(message: types.Message):
    img_dir = 'D:/pyth/pythonProject25/venv/pictures'
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, choice(img_list))
    file = types.FSInputFile(img_path)
    await message.answer_photo(photo=file)
