import sqlite3


class BotDataBase:

    def __init__(self, data_base_file):
        self.con = sqlite3.connect(data_base_file)
        self.cur = self.con.cursor()

    def check_user(self, user_id):
        check = self.cur.execute(
            '''SELECT id
                FROM users
                WHERE id = ?''',
            (user_id,)
        )
        return bool(len(check.fetchall()))

    def get_user_id(self, user_id):
        get_id = self.cur.execute(
            '''SELECT id
                FROM users
                WHERE id = ?''',
            (user_id,)
        )
        return get_id.fetchone()[0]

    def add_user_in_db(self, user_id, name, user_name):
        self.cur.execute(
            'INSERT INTO users(id, name, user_name) VALUES (?, ?, ?)',
            (user_id, name, user_name)
        )
        self.con.commit()
        return self.con.close()
