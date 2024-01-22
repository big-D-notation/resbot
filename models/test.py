import peewee as pw 
from models.base_model import BaseModel

class Test(BaseModel):
    id = pw.AutoField()
    title = pw.CharField()
    max_points = pw.IntegerField()
