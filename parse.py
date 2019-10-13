import sys
from spacy_lefff import LefffLemmatizer, POSTagger
import spacy
import pprint
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag


nltk.download('punkt')
nlp = spacy.load('fr')
french_lemmatizer = LefffLemmatizer()
nlp.add_pipe(french_lemmatizer, name='lefff', before='ner')


def main():
    sentence = sys.argv[1:]


    assert sentence, 'You must provide something'

    doc = nlp(u'%s' % sentence)

    persons = []
    organisations = []
    locations = []

    for entity in doc.ents:
        print('%s: %s' % (entity.label_, entity.text))
        if entity.label_ == 'PER':
            # Get only persons
            persons.append(entity.text)
        elif entity.label_ == 'LOC':
            # Get only locations
            locations.append(entity.text)
        elif entity.label_ == 'ORG':
            # Get only organisation
            organisations.append(entity.text)

    print_header('organisations')
    print(uniq(organisations))

    print_header('locations')
    print(uniq(locations))

    print_header('persons')
    print(uniq(persons))


def sanitize_chapter(chapter):
    """Remove some bad sring who don't want on """
    # clean chapter
    chapter = chapter.replace('\n', ' ')
    chapter = chapter.replace('_', '')
    return chapter


def uniq(array):
    """Remove duplicates entries from array"""
    return list(sorted(set(array)))


def print_header(title):
    """Print a beautifull header"""
    print("")
    print(title)
    print('=' * 80)


if __name__ == '__main__':
    main()
