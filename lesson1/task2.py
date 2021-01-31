import datetime
time_seconds = int(input("Введите время в секндах: "))
# Этот способ я нагуглил
print(datetime.timedelta(seconds=time_seconds))
# Это мой вариант
time_minutes = time_seconds//60
time_hours = time_minutes//60
print(f'{time_hours:02d}:{time_minutes%60:02d}:{time_seconds%60:02d}')
