def int_func(word):
    return word.title()


my_list = input('Введите строку из слов, разделенных пробелами: ').split()
for i in range(len(my_list)):
    my_list[i] = int_func(my_list[i])
print('Результат: ', ' '.join(my_list))