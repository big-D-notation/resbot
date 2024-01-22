from peewee import SqliteDatabase

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.db = SqliteDatabase('resbot.db')

        return cls._instance

    def get_connection(self):
        return self.db
