from operator import truediv

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['5', '7']
}


def ask_number_get_name(documents):
    input_number = input("Введите номер документа: ")
    for document in documents:
        if (document['number']) == input_number:
            return (document['name'])
    else:
        return "Номер документа отсутствует в базе данных!"


def ask_number_get_shelf(directories):
    input_number = input("Введите Номер Документа: ")
    for key, value in directories.items():
        for num in value:
            if input_number == num:
                a = str("Номер полки: ") + key
                return a
    else:
        return "Номер документа отсутствует в базе данных!"


def get_list_all_documents(documents):
    for document in documents:
        all_list_number_name = ('{} "{}" "{}"'.format(
            document['type'], document['number'], document['name']))
        print(all_list_number_name)


def add_new_document(documents, directories):
    type_document = input("Введите тип добовляемого документа: ")
    number_document = input("Введите номер добовляемого документа: ")
    owner_name_document = input(
        "Введите имя владельца добовляемого документа: ")
    shelf_number = input(
        "Введите номер полки, на котором будет храниться добовляемый документ: ")
    # Формируем словарь
    documents.append(
        {"type": type_document, "number": number_document, "name": owner_name_document})
    # Если такая полка не существует то она будет создана, новый номер полки для текущей записи добавляем в {directories}.
    add_new_shelf(directories, shelf_number)
    # Новый номер документ добавляем в {directories}  по ключу, в значения, в [list], в переменой shelf_number. (или) Добовляем в список, вложенный внутри словаря.")
    for key, value in directories.items():
        if shelf_number == key:
            value.append(number_document)
            print(" Запись успешно добавлена! \n Тип документ: {} \n Номер документа: {} \n Владелец: {} \n № полки хранения: {}\n".format(
                type_document, number_document, owner_name_document, shelf_number))
    return


def add_new_shelf(directories, shelf_number):
    if shelf_number not in directories:
        directories[shelf_number] = []
        print("\n Введеный номер полки", shelf_number,
              " добавлен в список! \n Список существующих полок: \n", list(directories.keys()))
    return


def del_document(documents, directories, number_document):
    for dic in documents:
        for key, value in dic.items():
            if number_document == value:
                documents.remove(dic)
    for key, value in directories.items():
        for item in value:
            if number_document == item:
                value.remove(item)
                print("\n Документ с №: {} удален! \n".format(number_document))
                return
    else:
        print("Документ с №: {} в каталоге не значится!".format(
            number_document))


def main(documents):
    while True:
        user_input = input("Введите команду: ").lower()
        if user_input == "p" or user_input == "people":
            print("\n", ask_number_get_name(documents), "\n")
        elif user_input == "s" or user_input == "shelf":
            print("\n", ask_number_get_shelf(directories), "\n")
        elif user_input == "l" or user_input == "list":
            if get_list_all_documents(documents) == None:
                print("\n")
        elif user_input == "a" or user_input == "add":
            if add_new_document(documents, directories) == None:
                print("\n")
        elif user_input == "as" or user_input == "add shelf":
            shelf_number = input("Введите номер полки: ")
            if add_new_shelf(directories, shelf_number) == None:
                print("\n")
        elif user_input == "d" or user_input == "del" or user_input == "delete":
            number_document = input("Введите номер удаляемого документа: ")
            if del_document(documents, directories, number_document) == None:
                print("\n")
        elif user_input == "dir":
            print(directories)
        elif user_input == "doc":
            print(documents)
        elif user_input == "m" or user_input == "move":
            print("\n", "move_document(documents)")
        elif user_input == "q" or user_input == "quit":
            print("\n", "До свидания!", "\n")
            break
        elif user_input != "p" or user_input != "people" or user_input != "s" or user_input != "shelf" or user_input != "l" or user_input != "list" or user_input != "a" or user_input != "add" or user_input != "d" or user_input != "delete" or user_input != "m" or user_input != "move" or user_input != "as" or user_input != "add shelf" or user_input != "q" or user_input != "quit":
            print("\n", "Введена не правильная команда!", "\n")


main(documents)
