from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards import start_keyboard, menu_keyboard


start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'привет {message.from_user.first_name}!', reply_markup=start_keyboard())


@start_router.callback_query(F.data == 'contacts')
async def about_us(callback: types.CallbackQuery):
    # await callback.answer('o nas')
    await callback.answer()
    await callback.message.answer_contact('+996 772 510 707\n', 'Империя Пиццы')
    await callback.message.answer_contact('+996 551 510 707\n', 'Империя Пиццы')


@start_router.callback_query(F.data == 'adress')
async def donate_us(callback: types.CallbackQuery):
    # await callback.answer('o nas')
    await callback.answer()
    await callback.message.answer('г.Бишкек, пр.Чуй, 92')


@start_router.callback_query(F.data == 'Menu')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='Вот наше меню', reply_markup=menu_keyboard())


@start_router.callback_query(F.data == 'food')
async def menu(callback: types.CallbackQuery):

    await callback.answer('Блюда скоро появятся в меню!')

# @start_router.callback_query(F.data == 'food1')
# async def menu(callback: types.CallbackQuery):
#     file = types.FSInputFile("D:/pyth/pythonProject25/images/pizza.jpg")
#     await callback.message.answer_photo(photo=file, caption=order_kb(), callback_data='order_1')


# @start_router.callback_query(F.data.startswith('order_'))
# async def order(callback: types.callback_query):
#     await callback.answer(f'В вашей корзине')

# @start_router.message(Command('myinfo'))
# async def start_cmd(message: types.Message):
#     img_dir = 'D:/pyth/pythonProject25/venv/pictures'
#     img_list = os.listdir(img_dir)
#     img_path = os.path.join(img_dir, choice(img_list))
#     file = types.FSInputFile(img_path)
#     await message.answer_photo(photo=file, caption=f'ваш id: {message.from_user.id} '
#                                                    f'ваше имя: {message.from_user.first_name} '
#                                                    f'ваш username: {message.from_user.username}')


# id_list = []
# handlers
# @dp.message(Command('start'))
# async def start_cmd(message: types.Message):
#     if message.from_user.id not in id_list:
#         id_list.append(message.from_user.id)
#     await message.answer(f'Привет! {message.from_user.first_name}, '
#                          f'наш бот обслуживает уже {len(id_list)} пользователя')
#
#
