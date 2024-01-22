import peewee as pw 
from models.base_model import BaseModel

class Student(BaseModel):
    id = pw.AutoField()
    name = pw.CharField()
    group = pw.CharField()
    tg_nick = pw.CharField()
