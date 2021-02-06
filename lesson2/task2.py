base_list = list(input("Введите значения списка через пробел: ").split(' '))
result_list = []
i = 1
if len(base_list) % 2 == 1:
    result_list.insert(len(base_list)-1, base_list[len(base_list)-1])
while i <= len(base_list)-1:
    result_list.insert(i-1, base_list[i])
    result_list.insert(i, base_list[i-1])
    i += 2
print("Результат: ", result_list)
