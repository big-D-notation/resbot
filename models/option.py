import peewee as pw

from models.base_model import BaseModel
from models.question import Question

class Option(BaseModel):
    id = pw.AutoField()
    question_id = pw.ForeignKeyField(Question, backref='questions')
    text = pw.CharField()
    is_right = pw.BooleanField()
