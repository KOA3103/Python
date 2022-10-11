from pprint import pprint


ids = {'user1': [213, 213, 3, 15, 213],
       'user2': [384, 584, 19, 119, 119],
       'user2': [54, 52, 59, 619, 9],
       'user2': [54, 51, 119, 119, 119],
       'user3': [213, 8, 98, 35]}

id_values = ids.values()
# print(id_values)  # вывел значения в списеке где вложены друние списки
# Проверка типа, в зависимости оттипа используем разные методы и функции.
# print(type(id_values))
# Создаем другой список в который будем помещать списки для обединения.
unique_id = []
for i in id_values:
    unique_id.extend(i)
pprint(set(unique_id))


# Дркгой вариант
ids = {'user1': [213, 213, 3, 15, 213],
       'user2': [384, 584, 19, 119, 119],
       'user2': [54, 52, 59, 619, 9],
       'user2': [54, 51, 119, 119, 119],
       'user3': [213, 8, 98, 35]}

uniq_ids = set()

for user in ids.values():
    for geo_data in user:
        uniq_ids.add(geo_data)
print(uniq_ids)
