import peewee as pw 

from models.base_model import BaseModel
from models.student import Student
from models.test import Test 

class Result(BaseModel):
    id = pw.AutoField()
    stud_tg = pw.ForeignKeyField(Student, backref='results')
    test_id = pw.ForeignKeyField(Test, backref='results')
    points = pw.FloatField()
    