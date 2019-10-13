import sys
from spacy_lefff import LefffLemmatizer, POSTagger
import spacy
import pprint
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

import logging



nltk.download('punkt')
nlp = spacy.load('fr')
french_lemmatizer = LefffLemmatizer()
nlp.add_pipe(french_lemmatizer, name='lefff', before='ner')


def parse_sentence(sentence):
    logger = logging.getLogger('parse_sentence')

    doc = nlp(u'%s' % sentence)

    persons = []
    organisations = []
    locations = []

    for entity in doc.ents:
        logger.debug('Found this entity: [%s] %s' % (entity.label_, entity.text))
        if entity.label_ == 'PER':
            persons.append(entity.text)
        elif entity.label_ == 'LOC':
            locations.append(entity.text)
        elif entity.label_ == 'ORG':
            organisations.append(entity.text)

    organisations = uniq(organisations)
    locations = uniq(locations)
    persons = uniq(persons)


def uniq(array):
    """Remove duplicates entries from array"""
    return list(sorted(set(array)))


if __name__ == '__main__':
    sentence = sys.argv[1:]
    assert sentence, 'You must provide something'

    parse_sentence(sentence)
