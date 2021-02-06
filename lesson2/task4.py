base_list = list(input("Введите строку из нескольких слов: ").split(' '))
for index in range(len(base_list)):
    if len(base_list[index]) > 10:
        print(index+1, ".", base_list[index][0:10])
    else:
        print(index+1, ".", base_list[index])
