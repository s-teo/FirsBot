import asyncio
from loader import dp, bot
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers import register_all_handlers

async def on_startup():
    await on_startup_notify(bot)
    await set_default_commands(bot)
    print("Бот запущен")

async def main():
    register_all_handlers(dp)
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
