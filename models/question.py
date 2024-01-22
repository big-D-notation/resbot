import peewee as pw

from models.base_model import BaseModel
from models.test import Test

class Question(BaseModel):
    id = pw.AutoField()
    test_id = pw.ForeignKeyField(Test, backref='questions')
    title = pw.CharField()
