import logging
from aiogram import Bot
from data.config import ADMINS_ID

async def on_startup_notify(bot: Bot):
    for admin in ADMINS_ID:
        try:
            text = 'Bot started'
            await bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
