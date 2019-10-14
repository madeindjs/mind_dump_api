from peewee import *
import datetime


db = SqliteDatabase('my_dumps.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

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


class Though(BaseModel):
    content = CharField(null=False)
    parsed = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    words = ManyToManyField(Word, backref='thoughwords')

    def export(self):
        return '%s - %s' % (self.created_at.strftime('%Y-%m-%d %H:%M'), self.sentence())

    def sentence(self):
        sentence = str(self.content)

        for word in self.words:
            sentence = sentence.replace(word.content, word.symbol())

        return sentence

    def to_object(self):
        return {
            'id': self.id,
            'content': self.content,
            'tags': [{'label': word.label, 'content': word.content} for word in self.words]
        }


ThoughWord = Though.words.get_through_model()


# class ThoughWord(BaseModel):
#     word = ForeignKeyField(Word)
#     though = ForeignKeyField(Though)


db.create_tables([Though, Word, ThoughWord])