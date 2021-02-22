# Я не понял, как ее решить, мой вариант не работает, решение из след. урока тоже
# Вернусь к ней позже и внимательнее изучу справку

import sys

hours, salary_per_our, bonus = map(float, sys.argv[1:])
print('Salary - {}'.format(hours * salary_per_our + bonus))

