import random

import pandas as pd

nick_names = pd.read_csv('../data/nicknames.csv')
classes = ['Воин', 'Стрелок', 'Маг', 'Призыватель', 'Некромант']
special = ['Сила', 'Восприятие', 'Выносливость', 'Харизма', 'Интеллект', 'Ловкость', 'Удача']
skills = ['Железный Кулак', 'Карманник', 'Прочность', 'Капиталист', 'Кровавое месиво', 'Ловец критов', 'Агент смерти']


def pretty(d, indent=0):
    if indent > 0:
        print()
    for key, value in d.items():
        print('\t' * indent + str(key) + ':', end='')
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def character_generator():
    character = {}
    rand = random.randint(0, nick_names.shape[0])
    nick_names.columns = list(map(lambda x: x.strip(), nick_names.columns))
    character['Имя'] = nick_names['name'].loc[nick_names.index[rand]].strip()
    character['Возраст'] = random.randint(0, 150)
    character['Класс'] = random.choice(classes)
    character['Параметры'] = {}
    for param in special:
        character['Параметры'][param] = random.randint(0, 10)

    character['Навыки'] = {}
    num_skills = random.randint(0, 10)
    cnt = 1
    for i in range(num_skills):
        x = random.choice(skills)
        if x not in character['Навыки'].values():
            character['Навыки'][cnt] = x
            cnt += 1
    return character


if __name__ == '__main__':
    pretty(character_generator())
