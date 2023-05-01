from aiogram import types

from create_bot import dp
from game.db.users_db import UserRegistration


async def start(message: types.Message):
	"""Происходит авмотатическая регистрация. Затем приветственное сообщение или же сообщение на команду /help."""

	# Регистрируем пользователя.
	UserRegistration.register(message.from_user.id, message.from_user.first_name)

	if message.text == '/start':
		await message.answer("Добро пожаловать.")
	elif message.text == '/help':
		await message.answer("У вас возникли проблемы или же вопросы ? Напишите нам: @Narek_76 / @Redpiar")


def register_handlers_game_launch(dp):
	"""Регистрируем обработчики(хендлеры) на команды, прописанные в этом файле(game_launch)."""
	dp.register_message_handler(start, commands=['start', 'help'])