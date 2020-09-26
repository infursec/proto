import telebot
import config
import strings as st
import keyboards as kb
import db
import re
from datetime import datetime
import qiwi
from telebot import types
import uuid
from random import randint

bot = telebot.TeleBot(config.token)

@bot.callback_query_handler(lambda query: query.data.startswith("check_"))
def stuff_callback(query):
	print(query.data.split("_"))
	task = db.get_task(query.data.split("_")[1])
	#добалвяем баланс пользователю
	#db.add_balance(query.message.from_user.id, task[1] )
	#уменьшаем у работодателя
	db.subs_balance(task[2], task[1])
	bot.send_message(task[2], "Задание {} выполнено".format(task[0]))
	#убираем заадние
	db.delete_task(task[0])
	bot.send_message(query.message.chat.id, "Задание успешно выполнено! На ваш счет зачислено {} CWD".format(task[1]))

@bot.callback_query_handler(lambda query: query.data.startswith("task_"))
def buy_callback(query):
	print(query.data.split("_"))
	task = db.get_task(query.data.split("_")[1])
	task_text = """Задание №{}
	Подпишитесь на канал - {} и получите {} CWD от {}"""
	bot.send_message(query.message.chat.id, task_text.format(task[0], task[3], task[1], task[2]), reply_markup=kb.check(task[0]))

def enter_channel(m, summ):
	print(m.text)
	bot.send_message(m.chat.id, "Задание опубликовано!")
	db.add_task(summ, m.from_user.id, m.text)

def enter_summ(m):
	print(m.text)
	a = bot.send_message(m.chat.id, "Введите ссылку на ваш канал")
	bot.register_next_step_handler(a, enter_channel, summ=m.text)

@bot.message_handler(commands=['start'])
def start(msg):
	print(msg.from_user.username)
	bot.send_message(msg.chat.id,st.start, reply_markup=kb.start)
	db.add_user(msg.from_user.id)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(msg):
	if msg.text == "Заработать":
		bot.send_message(msg.chat.id, "Выберите задание", reply_markup=kb.cats())

	elif msg.text == "Разместить рекламу":
		a = bot.send_message(msg.chat.id, "Введите, сколько будет оплата за задание")
		bot.register_next_step_handler(a, enter_summ)

	elif msg.text == "Баланс":
		usr = db.get_user(msg.from_user.id)
		usr_t = """Вы пользователь {}
		Баланс - {} CWD"""
		bot.send_message(msg.chat.id, usr_t.format(usr[0], usr[1]), reply_markup=kb.c)
if __name__ == '__main__':
    bot.polling(none_stop=True)
