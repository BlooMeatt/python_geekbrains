def my_func(a, b, c):
    sum_total = a + b + c
    min_value = a
    if b < min_value:
        min_value = b
    if c < min_value:
        min_value = c
    return sum_total - min_value


print(my_func(24, 25, 24))
