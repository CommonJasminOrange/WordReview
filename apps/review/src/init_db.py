import pandas as pd
import config

bookName = config.BOOK  # 请用英文
List_begin_num = config.begin_index  # 或 1，看你的 List 是从 0 开始还是 1 开始

'''
如果是 excel/csv，你应该有以下列
word 单词
mean 中文
List
Unit
Index
'''

path = config.excel_path
df = pd.read_excel(path)


def import_word(Review, BookList, Words):
    # path = config.excel_path
    # df = pd.read_excel(path)
    for i in range(0, (len(df))):
        dr = df.iloc[i]
        review_db = {
            'word': dr['word'],
            'LIST': dr['List'],
            'UNIT': dr['Unit'],
            'INDEX': dr['Index'],
            'BOOK': bookName,
        }
        print(i, dr['word'], dr['mean'])

        new_word = Review.objects.create(**review_db)
        new_word.save()

    # init_db_booklist(BookList, Review)
    # init_db_word(Review, Words)


def init_db_booklist(BookList, Review):
    for l in range(List_begin_num, List_begin_num + len(set(Review.objects.filter(BOOK=bookName).values_list('LIST')))):
        ld = Review.objects.filter(BOOK=bookName, LIST=l)  # list data
        if len(ld) == 0:
            print(f"List{l} has no content")
            continue
        print(l)
        # rate = sum([r[0] if r[0] is not None else 1 for r in ld.values_list('rate')
        #             ]) / len(ld) * 1
        # rate = 1 - rate if rate != 0.0 else 0
        data = {
            'LIST': l,
            'BOOK': bookName,
            # 'list_rate': rate,
            'word_num': len(ld),
            # 'review_word_counts': ';'.join(
            #     set([str(t[0]) for t in ld.values_list('total_num')])),
        }
        BookList.objects.create(**data)


def init_db_words(Review, Words):
    # path = config.excel_path
    # df = pd.read_excel(path)
    for i in range(0, (len(df))):
        dr = df.iloc[i]
        try:
            word = Words.objects.get(word=dr['word'])
            continue
        except:
            data = {
                'word': dr['word'],
                'mean': dr['mean'],
            }
            word = Words.objects.create(**data)
            print(word.word)
            word.save()


def init_db_books(Books):
    data = {
        'BOOK': config.BOOK,
        'BOOK_zh': config.BOOK_zh,
        'BOOK_abbr': config.BOOK_abbr,
        'begin_index': config.begin_index,
    }
    Books.objects.create(**data).save()
