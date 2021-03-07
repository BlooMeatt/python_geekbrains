# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.

class Cell:
    def __init__(self, cell_num):
        self.num = cell_num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        sub = self.num - other.num
        if sub > 0:
            return sub
        else:
            return 'Разница меньше нуля!'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num//other.num

    def make_order(self, lines):
        return '\n'.join(['X' * lines for i in range(self.num // lines)]) + '\n' + 'X' * (self.num % lines)


a = Cell(26)
b = Cell(14)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(10))
