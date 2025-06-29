from aiogram import Router, types
from aiogram.filters import Command

router = Router()

# @router.message(Command(commands=["help"]))
@router.message(lambda message: message.text.lower() == "привет" or Command("hello"))
async def command_start(message: types.Message):
    text = f"Привет, {message.from_user.first_name}!"
    await message.answer(text=text)
    print(text)