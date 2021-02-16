def new_func(a, b):
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        return a / b


x = int(input('Введите значение делимого: '))
y = int(input('Введите значение делителя: '))

print(new_func(x, y))
