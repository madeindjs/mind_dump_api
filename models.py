from peewee import *
import datetime


db = SqliteDatabase('my_dumps.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

class Though(BaseModel):
    content = CharField(unique=True)
    created_date = DateTimeField(default=datetime.datetime.now)
