# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random as r

# Функция создает строку случайного размера из случайных символов
def r_string():
    s = ''
    for i in range(r.randint(5, 10)):
        s = s + str(r.randint(1, 100)) + ' '
    return s.strip()


with open('task5.txt', 'w') as file:
    file.write(r_string())

with open('task5.txt') as file:
    line = file.readlines()
    print('Исходная строка:', " ".join(line))
    res = 0
    for i in line[0].split():
        res = res + int(i)
print('Сумма чисел в строке: ', res)
