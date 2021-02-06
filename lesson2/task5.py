base_list = [9, 8, 5, 3, 2, 1]
max_value = base_list[0]
min_value = base_list[len(base_list)-1]
new_element = int(input("Введите новый элемент рейтинга: "))
for index in range(len(base_list)):
    if new_element > max_value:
        base_list.insert(0, new_element)
        max_value = new_element
        break
    if new_element < min_value:
        min_value = new_element
        base_list.append(new_element)
        break
    if new_element == base_list[index]:
        base_list.insert(index, new_element)
        break
print("Новый рейтинг: ", base_list)
