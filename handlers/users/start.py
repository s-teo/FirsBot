from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=["start"]))
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nТвой ID: {message.from_user.id}")
