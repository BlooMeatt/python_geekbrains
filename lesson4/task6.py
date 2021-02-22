from itertools import cycle, count

for i in count(int(input('Введите начальное число: '))):
    if i > 100:
        break
    print(i)

my_list = cycle([1, 2, 3])
i = 0
while i < 100:
    print(next(my_list))
    i += 1