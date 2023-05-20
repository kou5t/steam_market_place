import logging

from settings import TOKEN
from sqlite_for_bot_pack.database_bot import BotDataBase as BotD
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    user_id = message['from']['id']
    user_first_name = message['from']['first_name']
    user_nik_name = message['from']['username']
    check = BotD('../test_base.sqlite').check_user(
        message['from']['id'],
    )

    if not check:
        add = BotD('../test_base.sqlite').add_user_in_db(
            user_id,
            user_first_name,
            user_nik_name
        )
        await message.reply(f'Привет {user_first_name}, кажется ты тут впервые')
    else:
        await message.reply(f'Привет {user_first_name}, кажется мы уже знакомы')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
