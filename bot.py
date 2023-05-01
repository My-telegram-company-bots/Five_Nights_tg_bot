from aiogram.utils import executor

from create_bot import dp
from game.handlers import (
	game_launch,
)


async def on_startup(_):
	"""Здесь будет идти подключение к БД."""
	print("Бот вышел в онлайн.")


# Подключаем к диспетчеру обработчики(хендлеры).
game_launch.register_handlers_game_launch(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)