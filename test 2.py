for key, value in directories.items():
    if shelf_number == key:
        value.append(number_document)
        result = (" Успешно добавлен: \n документ: {} \n №: {} \n вдалелец: {} \n № полки: {}\n".format(
            type_document, number_document, owner_name_document, shelf_number))


for key, value in directories.items():
    if shelf_number == key:
        value.append(number_document)
