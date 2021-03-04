# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} едет'.format(self.name))

    def stop(self):
        print('{} остановилась'.format(self.name))

    def turn(self, direction):
        print('{} поворачивает {}'.format(self.name, direction))

    def show_speed(self):
        print('Скорость: {}'.format(self.speed))


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Текущая скорость: {} Превышение скорости! Ограничение 60'.format(self.speed))


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Текущая скорость: {} Превышение скорости! Ограничение 40'.format(self.speed))


class PoliceCar(Car):
    pass


town_car = TownCar(85, 'Green', 'Opel', False)
sport_car = SportCar(200, 'Red', 'Ferrari', False)
work_car = WorkCar(60, 'White', 'Ford', False)
police_car = PoliceCar(140, 'Black', 'Chevrolet', True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
police_car.turn('налево')
