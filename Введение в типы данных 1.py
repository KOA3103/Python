boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys) == len(girls):
    print("1 Идеальные пары:")
    i = 2
    for name_boy, name_girl in zip(boys, girls):
        print(i, name_boy, " и ", name_girl)
        i += 1
else:
    print("Количество людей в списках не совпадает, мы никого знакомить не будем, потому что кто-то может остаться без пары!")
