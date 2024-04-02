from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message)
    await message.answer('неизветная команда!'
                         'попробуйте следующие команды:\n'
                         '/start /random_pic /myinfo')
