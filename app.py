import asyncio

from utils.crypto_user_main import hour_earning
from utils.get_current_crypto import get_price
from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    # print("Чистим базу")
    # await db.gino.drop_all()
    #
    # print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()

    print("Готово")
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    loop = asyncio.get_event_loop()
    loop.create_task(get_price())
    loop.create_task(hour_earning())

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
