input_number = input("Введите целое положительное число: ")
str_length = len(input_number)
highest_number = int(input_number[0])
i = 0
while i < str_length:
    if int(input_number[i]) > highest_number:
        highest_number = int(input_number[i])
    i += 1
print("Самая большая цифра в числе: ", highest_number)
