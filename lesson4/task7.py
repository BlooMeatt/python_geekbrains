from math import factorial
from itertools import count


def fibo():
    for el in count(1):
        yield factorial(el)


for n, i in enumerate(fibo(), start=1):
    print('Факториал числа ', n, ' равен ', i)
    if n == 15:
        break
