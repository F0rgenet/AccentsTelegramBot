import configparser
import logging.config

from aiogram import Bot, Dispatcher, executor, types

from database.database import DataBase

# logging
# Исправить логирование
logging.config.fileConfig('config/logging.conf')
bot_logger = logging.getLogger('bot')
database_logger = logging.getLogger('database')

# database
users = DataBase('database/users.db')

# config
# Сделать конфиг удобным
config = configparser.ConfigParser()
config.read('config/config.ini')
telegram_config = config['Telegram']

# bot
bot = Bot(telegram_config['token'])
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands='start')
async def start(message: types.Message):
	await message.reply("-")


@dispatcher.message_handler()
async def handle(message: types.Message):
	bot_logger.info(f"{message.from_user.full_name}:\"{message.text}\" link:'{message.from_user.url}'")
	if not message.migrate_from_chat_id == config["Administrators"] or not config["debug"]:  # исправить
		await message.forward(1108411521, True)


if __name__ == "__main__":
	executor.start_polling(dispatcher)