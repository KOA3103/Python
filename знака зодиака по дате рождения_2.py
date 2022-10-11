month = str(input("Введите месяц рождения: ")).lower()
date = int(input("Введите день рождения: "))
print()
print("Вывод: ")
if month == "март" or month == "march" or month == "3" or month == "03":
    if 1 <= date <= 20:
        print("Рыбы")
    elif 21 <= date <= 31:
        print("Овен")
elif month == "апрель" or month == "april" or month == "4" or month == "04":
    if 1 <= date <= 20:
        print("Овен")
    elif 21 <= date <= 30:
        print("Teлeц")
elif month == "май" or month == "5" or month == "05":
    if 1 <= date <= 21:
        print("Teлeц")
    elif 22 <= date <= 31:
        print("Близнeцы")
elif month == "июнь" or month == "6" or month == "06":
    if 1 <= date <= 21:
        print("Близнeцы")
    elif 22 <= date <= 30:
        print("Paк")
elif month == "июль" or month == "7" or month == "07":
    if 1 <= date <= 22:
        print("Paк")
    elif 23 <= date <= 31:
        print("Лeв")
elif month == "август" or month == "8" or month == "08":
    if 1 <= date <= 22:
        print("Лeв")
    elif 23 <= date <= 31:
        print("Дева")
elif month == "сентябрь" or month == "9" or month == "09":
    if 1 <= date <= 22:
        print("Дева")
    elif 23 <= date <= 30:
        print("Весы")
elif month == "октябрь" or month == "10":
    if 1 <= date <= 22:
        print("Весы")
    elif 23 <= date <= 31:
        print("Скорпион")
elif month == "ноябрь" or month == "11":
    if 1 <= date <= 22:
        print("Скорпион")
    elif 23 <= date <= 30:
        print("Стрелец")
elif month == "декабрь" or month == "12":
    if 1 <= date <= 21:
        print("Стрелец")
    elif 22 <= date <= 31:
        print("Козерог")
elif month == "январь" or month == "1" or month == "01":
    if 1 <= date <= 20:
        print("Козерог")
    elif 21 <= date <= 31:
        print("Водолей")
elif month == "февраль" or month == "2" or month == "02":
    if 1 <= date <= 19:
        print("Водолей")
    elif 20 <= date <= 28:
        print("Рыбы")
