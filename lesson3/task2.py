def my_func(**kwargs):
    res = ''
    for key in kwargs:
        res = res + str(kwargs.get(key)) + ' '
    return res


print(my_func(name='Valeriy', surname='Mazhuga', bd=1995, city='Moscow', email='johndoe@mail', phone='123456789'))
