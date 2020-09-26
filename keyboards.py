import telebot
import db
from telebot import types
start = types.ReplyKeyboardMarkup(resize_keyboard=True)
start.add(types.KeyboardButton("Заработать"),
		types.KeyboardButton("Разместить рекламу"),
		types.KeyboardButton("Баланс") )

back = types.InlineKeyboardMarkup()
back.add(types.InlineKeyboardButton(text="Назад", callback_data="game_back"))


def cats():
	print("c")
	#здесь должен быть блокчейн но увы
	cities = db.get_tasks()
	lk = types.InlineKeyboardMarkup()
	for c in cities:
		print(c)
		lk.add(types.InlineKeyboardButton(text="Подписаться на {} - {} CWD".format(c[3], c[1]), callback_data="task_{}".format(c[0])))
	return lk

c = types.InlineKeyboardMarkup()
c.add(types.InlineKeyboardButton(text="Пополнить", callback_data="lk_1"))
c.add(types.InlineKeyboardButton(text="Вывести", callback_data="lk_2"))


def check(m):
	c = types.InlineKeyboardMarkup()
	c.add(types.InlineKeyboardButton(text="Проверить задание", callback_data="check_{}".format(m)))
	return c