queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'завтра пойти гулять с котом'
]

dic = {}

for i in queries:
    words = i.split()
    if len(words) in dic.keys():
        dic[len(words)] += 1
    else:
        dic.update({len(words): 1})

for key, value in dic.items():
    percent = (value / len(queries)) * 100
    print('Поисковых запросов из', key, 'слов -', percent, '%')
