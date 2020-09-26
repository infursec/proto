import sqlite3
conn = sqlite3.connect('base.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id text, balance text)''')

c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY NOT NULL, summ text, giver text, channel text)''')

c.execute('''CREATE TABLE IF NOT EXISTS stuff
             (id INTEGER PRIMARY KEY NOT NULL, name text, cat text, amount text, price text, descr text, stuff text )''')

#-----GET-----


def get_user(uid):
	c.execute("""SELECT * FROM users WHERE id=?""", [(uid)])
	conn.commit()
	return c.fetchone()


def get_tasks():
	c.execute("""SELECT * FROM tasks""")	
	conn.commit()
	return c.fetchall()

def get_task(wid):
	q = """SELECT * FROM tasks WHERE id=?"""
	c.execute(q, [(wid)])
	conn.commit()
	return c.fetchone()
def delete_task(wid):
	q = """DELETE from tasks WHERE id=?"""
	c.execute(q, [(wid)])
	conn.commit()


#-----GET-----


#-----ADD-----
def add_user(uid):
	c.execute("""INSERT INTO users VALUES (?, 0)""", [(uid)])
	conn.commit()

def add_balance(uid, summ):
	q0 = """SELECT * FROM users WHERE id=?"""
	c.execute(q0, [(uid)])
	conn.commit()
	balance = c.fetchone()[1]
	print(balance)
	new_balance = int(balance) + int(summ)
	q = """UPDATE users SET balance=? WHERE id=?"""
	c.execute(q, (new_balance, uid))
	conn.commit()

def subs_balance(uid, summ):
	q0 = """SELECT * FROM users WHERE id=?"""
	c.execute(q0, [(uid)])
	conn.commit()
	balance = c.fetchone()[1]
	print(balance)
	new_balance = int(balance) - int(summ)
	q = """UPDATE users SET balance=? WHERE id=?"""
	c.execute(q, (new_balance, uid))
	conn.commit()


def add_task(summ, giver,channel):
	c.execute("""INSERT INTO tasks VALUES (NULL, ?,?,?)""", (summ, giver,channel))
	conn.commit()
#-----ADD-----


def get_user(uid):
	q = """SELECT * FROM users WHERE id=?"""
	c.execute(q, [(uid)])
	conn.commit()
	return c.fetchone()
def get_user_by_name(uid):
	q = """SELECT * FROM users WHERE username=?"""
	c.execute(q, [(uid)])
	conn.commit()
	return c.fetchone()
