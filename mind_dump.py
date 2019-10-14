import sys
from mind_dump.models import Though, Word, ThoughWord
from mind_dump.parse import parse_sentence
from sqlite3 import IntegrityError


if __name__ == '__main__':

    if sys.argv[1:]:
        sentences = sys.argv[1:][0]
    elif sys.stdin:
        sentences = ""
        for line in sys.stdin:
            sentences += line

    assert sentences, 'You must provide something'



    for sentence in sentences.splitlines():
        though = Though.create(content=sentence)

        for entity in parse_sentence(sentence):
            word = None

            try:
                word = Word.get(Word.content == entity.text)
            except:
                word = Word.create(label=entity.label_, content=entity.text)

            try:
                though_word = ThoughWord.create(word=word, though=though)
                though_word.save()
            except:
                pass


    though.parsed = True
    though.save()

