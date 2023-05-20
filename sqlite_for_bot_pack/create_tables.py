import sqlite3

con = sqlite3.connect('../test_base.sqlite')
cur = con.cursor()

table_users = '''CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT,
    user_name TEXT
);
'''

table_requests = '''CREATE TABLE IF NOT EXISTS requests(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    request TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE 
    );
    '''

cur.execute(table_users)
cur.execute(table_requests)
con.close()
