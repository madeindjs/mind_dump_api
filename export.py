from mind_dump.models import Though, Word, ThoughWord

if __name__ == '__main__':
    thoughs = (Though.select())

    for though in thoughs:
        print(though.export())