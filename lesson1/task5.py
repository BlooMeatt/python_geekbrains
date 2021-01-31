income = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек фирмы: "))
profit = income - costs
if profit > 0:
    print("Ваша фирма вышла с прибылью")
    print("Рентабельность выручки составила", profit/income)
    staff = int(input("Введите количество сотруднков: "))
    print("Прибыль в пересчете на одного сотрудника составила: ", profit/staff)
else:
    print("Ваша фирма вышла с убытками")
