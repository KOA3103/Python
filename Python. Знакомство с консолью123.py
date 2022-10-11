length_square = int(input("Введите длину стороны квадрата: "))
print()
print("Вывод: ")
perimeter_square = length_square * 4
print("Периметр: ", perimeter_square)
square_area = length_square * length_square
print("Площадь: ", square_area)
print()
length_rectangle = int(input("Введите длину прямоугольника: "))
width_rectangle = int(input("Введите ширину прямоугольника: "))
print()
print("Вывод: ")
perimeter_rectangle = (length_rectangle + width_rectangle) * 2
print("Периметр: ", perimeter_rectangle)
square_rectangle = length_rectangle * width_rectangle
print("Площадь: ", square_rectangle)
print()

simbol = input("Введите символ: ")
print(simbol * (perimeter_square + square_rectangle))
print()

wages = int(input("Введите заработную плату в месяц: "))
mortgage = int(input("Введите, какой процент(%) уходит на ипотеку: "))
for_life = int(input("Введите, какой процент(%) уходит на жизнь: "))
mortgage_expenses = int(wages * 12 * mortgage / 100)
life_expenses = int(wages * 12 * for_life / 100)
wages_year = wages * 12
print()
print("Вывод: ")
print("Вычисляем траты на ипотеку за год: ", mortgage_expenses, "рублей")
print("Вычисляем траты на жизнь за год: ", life_expenses, "рублей")
print("Заработано за год: ", wages_year, "рублей")
print("На ипотеку было потрачено: ", mortgage_expenses, "рублей")
print("Было накоплено: ", wages_year - mortgage_expenses - life_expenses, "рублей")

