from mind_dump.models import Though, Word, ThoughWord

if __name__ == '__main__':
    thoughs = (
        Though.select(Word.label, Word.content, Though.content, Though.created_at)
            .join(ThoughWord)
            .join_from(ThoughWord, Word)
    )

    for though in thoughs:
        print(though.export())