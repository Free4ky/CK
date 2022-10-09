from random import choice, random


def word_generator():
    print('Стоп слово - красный')
    word = input()
    while word != 'красный':
        yield word
        word = input()


def sentence_generator():
    print('Введите существительные:')
    nouns = [i for i in word_generator()]
    print('Введите глаголы:')
    verbs = [i for i in word_generator()]
    phrase_number = int(input('Введите количество фраз:'))
    for _ in range(phrase_number):
        r = random()
        if r <= 0.3:
            yield f'{choice(nouns)} {choice(verbs)} {choice(nouns)}'  # сгс
        elif 0.3 < r < 0.6:
            yield f'{choice(verbs)} {choice(nouns)} {choice(nouns)}'  # гсс
        else:
            yield f'{choice(nouns)} {choice(nouns)} {choice(verbs)}'  # ссг
