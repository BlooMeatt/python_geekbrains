daily_result = int(input("Введите результат первого дня: "))
result_km = int(input("Введите значение требуемого результата: "))
day = 1
while daily_result < result_km:
    print(daily_result)
    daily_result = daily_result + daily_result * 0.1
    day += 1
print("Резульатат в ", result_km, " km будет достигнут на ", day, " день")
