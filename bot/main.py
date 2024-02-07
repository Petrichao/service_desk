import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.handlers.user_commands import router as user_command_router


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Запуск процесса поллинга новых апдейтов
async def main():
    # Объект бота
    bot = Bot(
        token='6850389232:AAGm_wTL8y4OHrOv7jUOEvTdFwZYnzPw-W4',
        parse_mode='HTML'
    )
    # Диспетчер
    dp = Dispatcher()
    dp.include_routers(
        user_command_router,
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
