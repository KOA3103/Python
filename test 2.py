k = [800, 100, 2, 4, 6, 3, 9]
for i in k:
    if i % 2 == 0:
        # print(i)
        k.remove(i)
    else:
        # k.extend(i)
print(k)
