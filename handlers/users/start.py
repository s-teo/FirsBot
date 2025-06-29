# aiogram 3.x.x
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def command_start(message: types.Message):
    text = f"Привет, {message.from_user.first_name}!\nТвой ID: {message.from_user.id}"
    await message.answer(text=text)
    print(text)


# aiogram 2.x.x
# from aiogram import types
# from loader import dp
#
# @dp.message_handler(commands="start")
# async def command_start(message: types.Message):
#     await message.answer(f'Привет {message.from_user.first_name}! \n'
#                          f'Твой ID: {message.from_user.id}')