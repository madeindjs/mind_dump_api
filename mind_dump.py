import sys
from models import Though
from parse import parse_sentence


if __name__ == '__main__':
    sentence = sys.argv[1:]
    assert sentence, 'You must provide something'

    parse_sentence(sentence)