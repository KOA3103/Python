#  Словарь, по значению выбираем ключ: print(get_key(33, test_dict)), и по ключу выбипаем значение: print(test_dict['1']).

test_dict = {
    '1': 11,
    '2': 22,
    '3': 33
}


def get_key(base_value, a):
    for key, value in a.items():
        if base_value == value:
            return key


print(get_key(33, test_dict))  # Словарь, по значению выбираем ключ
print(test_dict['1'])  # и по ключу выбипаем значение
