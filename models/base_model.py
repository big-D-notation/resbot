from peewee import Model

from utils.database import Database


class BaseModel(Model):
    class Meta:
        database = Database().get_connection()
