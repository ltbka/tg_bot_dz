import asyncio
import os
from aiogram import Bot, Dispatcher, types
from os import getenv
import logging

from config import bot, dp, set_my_menu
from Handlers.start import start_router
from Handlers.picture import pic_router
from Handlers.generic_answer import echo_router
from Handlers.shop import shop_router
async def main():

    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(shop_router)
    dp.include_router(echo_router)

    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())