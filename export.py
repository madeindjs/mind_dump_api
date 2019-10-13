from mind_dump.models import Though, Word, ThoughWord

if __name__ == '__main__':
    thoughs = (
        Though.select(Word.label, Word.content, Though.content, Though.created_date)
            .join(ThoughWord)
            .join_from(ThoughWord, Word)
    )

    # .join_from(Tweet, User)

    for though in thoughs:
        print(though.export())
        # print(though.thoughword.word.symbol())
        # print(though.thoughword.word.label)