def my_func(x, y):
    if y == 0:
        return 1
    res = x
    for i in range(y - 1):
        print(res)
        res = x * res
    return res


print(my_func(2, 10))
print(2 ** 10)
