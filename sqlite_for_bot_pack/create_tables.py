import sqlite3

con = sqlite3.connect('test_base.sqlite')

cur = con.cursor()

query_1 = '''CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    user_name TEXT,
    telegram_id INTEGER
);
'''

cur.execute(query_1)

con.close()