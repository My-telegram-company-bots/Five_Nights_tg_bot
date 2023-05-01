import sqlite3


# Создаем БД или же подключаемся к ней.
conn = sqlite3.connect("game.db")

# Создаем обьект cursor.
cur = conn.cursor()

# Создаем таблицу users в БД.
cur.execute("""CREATE TABLE IF NOT EXISTS users(
	tg_id INTEGER PRIMARY KEY,
	tg_user_name INTEGER);
""")

# Сохраняем изменения.
conn.commit()


class UserRegistration():
	"""Регистрируем пользователей."""

	def register(tg_id, tg_user_name):
		"""Регистрируем новых пользователей."""
		
		# Проверка на то, зарегестрирован ли пользователь или нет.
		if cur.execute("SELECT * FROM users WHERE tg_id=?", (tg_id,)) == None:

			# Добавляем данные в нашу табличку users.
			cur.execute("""INSERT INTO users VALUES(?, ?);""", (tg_id, tg_user_name))
			# Сохраняем изменения.
			conn.commit()

			print("Пользователь зарегестрирован!")

		else:
			print("Пользователь уже был зарегестрирован!")
