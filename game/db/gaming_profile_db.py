import sqlite3


# Создаем БД или же подключаемся к ней.
conn = sqlite3.connect("game.db")

# Создаем обьект cursor.
cur = conn.cursor()

# Создаем таблицу БД.
cur.execute("""CREATE TABLE IF NOT EXISTS gaming_profile(
	tg_id INTEGER PRIMARY KEY,
	victories INTEGER,
	losses INTEGER,
	experience INTEGER,
	number_of_rounds INTEGER);
""")


class AddDataToGameProfile():
	"""Добавление данных в игровой профиль пользователя."""

	def add_data_to_game_profile(self, victories, losses, experience, number_of_rounds):
		"""Добавления игровых данных пользователя."""

		# Добавляем данные в нашу табличку gaming_profile.
		cur.execute("""INSERT INTO gaming_profile VALUES(?, ?, ?, ?, ?);""", (victories, losses, experience, number_of_rounds))
		# Сохраняем изменения.
		cur.commit()