from aiogram import types
from aiogram import Bot

# Дефолтные команды которые отображаются при вводе слеша (/)
async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Start bot"),
        types.BotCommand(command="help", description="Help"),
        types.BotCommand(command="hello", description="Поздороваться"),
    ])
