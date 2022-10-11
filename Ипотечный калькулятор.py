base_interest_rate = 7.5  # на 29.09.2022
print("---------------------                              ")
print("Ключевая ставка, установленная Банком России с 19 сентября 2022 года: ",
      base_interest_rate, "%")
print("---------------------                              ")
print()

discount_children = 0
discount_client_bank = 0
discount_insurance = 0


region = input("Введите регион проживания: ").lower()
print()
print("---------------------                              ")
if region == "дальний восток":
    print("Поздравляем! Ваша базовая процентная ставка становится 2%")
    print()
    print("---------------- the end ------------  ")
    print()
else:
    children = int(input("Сколько у вас детей? "))
    if children >= 4:
        discount_children -= 1
    client_bank = input(
        "Вы зарплатный клиент нашего банка (да/нет, yes/no): ").lower()
    if client_bank == "да" or client_bank == "yes":
        discount_client_bank -= 0.5
    insurance = input("Вы застрахованы в нашем банке? (да/нет): ").lower()
    if insurance == "да" or insurance == "yes":
        discount_insurance -= 1.5
    final_interest_rate = base_interest_rate + discount_children + \
        discount_client_bank + discount_insurance
    print("Ваша финальная процентная ставка по ипотеке: ",
          final_interest_rate, "%")
    print(type(insurance))
