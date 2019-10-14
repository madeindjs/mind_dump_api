from mind_dump.models import Though

if __name__ == '__main__':
    thoughs = (Though.select())

    for though in thoughs:
        print(though.export())