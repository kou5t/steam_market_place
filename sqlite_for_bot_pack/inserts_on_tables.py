import sqlite3

con = sqlite3.connect('test_base.sqlite')

cur = con.cursor()
# user ожидает кортеж с данными пользователя
user = ('Andrey Dogadkin', 'jvgger', 400044499303)

cur.execute(
    'INSERT INTO users(id, name, user_name) VALUES(?, ?, ?);',
    user
)
con.commit()
con.close()
