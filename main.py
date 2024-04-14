import asyncio
import logging
from aiogram import Dispatcher
from database import db
from handlers import start, order, apply_project, apply_no_project
from settings.settings import bot

# Диспетчер
dp = Dispatcher()
# вариант регистрации роутеров по одному на строку
dp.include_router(start.router)
dp.include_router(apply_project.router)
dp.include_router(apply_no_project.router)
dp.include_router(order.router)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# подключаем базу данных
async def on_startup():
    await db.db_start()
    print('бот успешно запущен!')


async def main():
    # подключение к БД до запуска бота
    await on_startup()
    await bot.delete_webhook(drop_pending_updates=True)
    # Запуск процесса поллинга новых апдейтов
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

