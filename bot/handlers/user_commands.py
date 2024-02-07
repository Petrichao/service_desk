from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from bot.keyboards.keyboards import start_kb

router = Router()


# Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        f'Hello!, '
        f'{message.from_user.id}, '
        f'{message.from_user.first_name}, '
        f'{message.from_user.last_name}'
        f'{message.from_user.username}',
        reply_markup=start_kb,
    )


# Хэндлер на команду создания тикета /createnewticket
@router.message(Command('create_new_ticket'))
async def cmd_create_new_ticket(message: Message):
    pass
