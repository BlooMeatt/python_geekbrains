flag = 1
total_sum = 0
while flag > 0:
    my_lis = input('Введите числа через проблел. ! для завершения: ').split()
    summa = 0
    for i in my_lis:
        if i == '!':
            flag = 0
            break
        summa = summa + int(i)
    total_sum = total_sum + summa
    print('Сумма чисел: ', total_sum)
