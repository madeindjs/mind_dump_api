import sys
from models import Though, Word, ThoughWord
from parse import parse_sentence


if __name__ == '__main__':
    sentence = sys.argv[1:][0]
    assert sentence, 'You must provide something'

    though = Though.create(content=sentence)

    for entity in parse_sentence(sentence):

        word = None

        try:
            word = Word.get(Word.content == entity.text)
        except:
            word = Word.create(label=entity.label_, content=entity.text)

        though_word = ThoughWord.create(word=word, though=though)
        though_word.save()

    though.parsed = True
    though.save()

