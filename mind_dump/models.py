from peewee import *
import datetime


db = SqliteDatabase('my_dumps.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

class Though(BaseModel):
    content = CharField(null=False)
    parsed = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.datetime.now)

    def export(self):
        word = self.thoughword.word
        return str(self.content).replace(word.content, word.symbol())


class Word(BaseModel):
    label = CharField(null=False)
    content = CharField(null=False)

    def symbol(self):
        labels = {
            'PER': '+',
            'LOC': '@',
            'ORG': ':',
            'MISC': '?'
        }

        return '%s[%s]' % (labels.get(self.label), self.content)

class ThoughWord(BaseModel):
    word = ForeignKeyField(Word)
    though = ForeignKeyField(Though)


db.create_tables([Though, Word, ThoughWord])