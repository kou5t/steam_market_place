import sqlite3

con = sqlite3.connect('../test_base.sqlite')
cur = con.cursor()

query_1 = '''CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT,
    user_name TEXT
);
'''

cur.execute(query_1)
con.close()
