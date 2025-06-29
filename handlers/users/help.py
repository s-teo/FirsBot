from aiogram import Router, types
from aiogram.filters import Command


router = Router()

@router.message(Command("help"))
async def help_command(message: types.Message):
    help_text = (
        "/start - Запустить бота\n"
        "/help - Показать список команд\n"
        "/hello - Поздороваться\n"
    )
    await message.answer(help_text)