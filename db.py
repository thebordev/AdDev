import sqlite3
from datetime import datetime

class Users:
    def __init__(self, dbname='addev.db'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        table = ("""CREATE TABLE IF NOT EXISTS USERS (
        user_id INT NOT NULL,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        group_id TEXT,
        reg_time TEXT
        )""")

        self.conn.execute(table)
        self.conn.commit()

    def register_user(self, user_id, username, first_name, last_name):
        user = self.conn.cursor().execute(f"SELECT * FROM USERS WHERE user_id = {user_id};").fetchall()
        if not user:
            user_data = self.conn.cursor().execute(f'INSERT INTO USERS (user_id, username, first_name, last_name, reg_time) VALUES ({user_id}, "{username}", "{first_name}", "{last_name}", "{datetime.now()}");')
            self.conn.commit()
            print("Пользователь " + str(user_id) + " зарегистрирован!")

    def add_channel_user(self, user_id, channel_username):
        data = f"UPDATE USERS SET group_id = {channel_username} WHERE user_id = {user_id}"
        self.conn.cursor().execute(data)
        self.conn.commit()

class Channels:
    def __init__(self, dbname='addev.db'):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        table = ("""CREATE TABLE IF NOT EXISTS CHANNELS (
        channel_id INT NOT NULL,
        channel_username TEXT,
        channel_name TEXT,
        user_id_owner INT NOT NULL,
        username_owner TEXT,
        subs INT,
        stars INT,
        reviews TEXT,
        completed INT,
        canceled INT,
        status TEXT,
        active TEXT,
        offer TEXT,
        reg_time TEXT
        )""")

        self.conn.execute(table)
        self.conn.commit()

    def register_channel(self, channel_id, channel_useranme, channel_name, user_id_owner, username_owner, subs):
        data = f"SELECT * FROM CHANNELS WHERE channel_id = {channel_id};"
        channel = self.conn.cursor().execute(data).fetchall()
        if not channel:
            register_data = f'INSERT INTO CHANNELS (channel_id, channel_username, channel_name, user_id_owner, username_owner, subs, stars, completed, canceled, status, reg_time) VALUES ({channel_id}, "{channel_useranme}", "{channel_name}", {user_id_owner}, "{username_owner}", {subs}, {int(0)}, {int(0)}, {int(0)}, "OK", "{datetime.now()}");'
            self.conn.cursor().execute(register_data)
            self.conn.commit()
            print(f"Канал {channel_useranme} зпрегистрирован!")

if __name__ == '__main__':
    Channels().setup()
    Users().setup()