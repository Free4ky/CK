import re
import difflib
from task2 import word_generator

d = "' ',.!?/&-:;@'..."
delims = "[" + "\\".join(d) + "]"


def diff():
    print('Введите корректные слова:')
    correct_words = list(map(lambda x: x.lower(), [i for i in word_generator()]))
    #correct_words = list(map(lambda x: x.lower(), ['Морковь', 'Чай', 'Хлеб', 'Магазин']))
    sentence = re.split(delims, input('Введите предложение:'))
    #sentence = re.split(delims, 'Недавно я ходил в могозин и купил: марковь, хлиб, чай')
    closest = {}
    for word in correct_words:
        closest[word] = difflib.get_close_matches(word, sentence)[0]

    wrong_indexes = {}
    for correct_word, wrong_word in closest.items():
        i = 0
        for s in difflib.ndiff(wrong_word, correct_word):
            if s[0] == '-':
                if wrong_word in wrong_indexes.keys():
                    wrong_indexes[wrong_word].append(i)
                else:
                    wrong_indexes[wrong_word] = [i]
            if s[0] == '+':
                i -= 1
            i += 1
    result = []
    for word, wrong_indexes_list in wrong_indexes.items():
        l_word = []
        l_word.extend(word)
        for i in wrong_indexes_list:
            l_word[i] = f' {l_word[i]} '
        result.append(''.join(l_word))

    return result

if __name__ == '__main__':
    print(diff())
