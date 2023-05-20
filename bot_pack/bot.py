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

DB_PATH = '../test_base.sqlite'


def check_and_add(user_id, user_f_name, user_nik_name):
    check = BotD(DB_PATH).check_user(
        user_id,
    )
    if not check:
        add = BotD(DB_PATH).add_user_in_db(
            user_id,
            user_f_name,
            user_nik_name
        )
        return check
    else:
        return check


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_id = message['from']['id']
    user_first_name = message['from']['first_name']
    user_nik_name = message['from']['username']
    check = check_and_add(user_id, user_first_name, user_nik_name)
    if not check:
        await message.reply(f'Привет {user_first_name}, кажется ты тут впервые')
    else:
        await message.reply(f'Привет {user_first_name}, кажется мы уже знакомы')


@dp.message_handler(commands=['+', 'add'])
async def add_user_request(message: types.Message):
    user_id = message['from']['id']
    user_command_list = message.text.split()[1:]
    # Добавить нормальную проверку на пустое сообщение
    if user_command_list:
        user_request = ' '.join(user_command_list)
        BotD(DB_PATH).add_user_requests(user_id, user_request)
        await message.reply('Ваш запрос добавлен в избранное')
    else:
        await message.reply('Ваш запрос пуст')


@dp.message_handler(commands=['favorites', 'f'])
async def add_user_request(message: types.Message):
    user_id = message['from']['id']
    mess = BotD(DB_PATH).get_user_requests(user_id)
    answer = 'Ваши избранные запросы:\n'
    for i in mess:
        for p in i:
            answer += p + '\n'
    await message.reply(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
