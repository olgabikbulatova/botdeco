from aiogram import Bot
from config_reader import config


# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
admin_id = config.admin_id.get_secret_value()




