# Задание 1

import time

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
       if self.__color == 'red':
            print('red')
            time.sleep(7)
            print('yellow')
            time.sleep(2)
            print('green')
            time.sleep(5)
       elif self.__color == 'yellow':
            print('yellow')
            time.sleep(2)
            print('green')
            time.sleep(5)
            print('red')
            time.sleep(7)
       else:
            print('green')
            time.sleep(5)
            print('red')
            time.sleep(7)
            print('yellow')
            time.sleep(2)

traffic_light_1 = TrafficLight('green')
traffic_light_1.running()

# Задание 2

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass_per_sqmeter = 25
        thickness = 5
        result = self._length * self._width * mass_per_sqmeter * thickness
        print(f'Масса асфальта, необходимая для покрытия дороги длиной {self._length}м и шириной {self._width}м, составляет {result}т.')

road_1 = Road(100, 20)
road_1.asphalt_mass()

# Задание 3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = wage
        self._bonus = bonus

class Position(Worker):

    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        income = {'wage': self._wage, 'bonus': self._bonus}
        sum_ = sum(income.values())
        print(f'Доход сотрудника с учетом премии: {sum_}')

worker_1 = Position('Анна', 'Иванова', 'Manager', 80000, 20000)
worker_1.get_full_name()
worker_1.get_total_income()

# Задание 4

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car goes')

    def stop(self):
        print('Car stops')

    def turn(self, direction):
        print(f'Car turns to the {direction}')

    def show_speed(self):
        print(f"Car's speed is {self.speed}km")

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Car's speed is {self.speed}km. Above speed limit!")
        else:
            print(f"Car's speed is {self.speed}km")

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Car's speed is {self.speed}km. Above speed limit!")
        else:
            print(f"Car's speed is {self.speed}km")

class PoliceCar(Car):
    pass

t1 = TownCar(70, 'white', 'Mazda', False)
s1 = SportCar(150, 'yellow', 'Mazeratti', False)
w1 = WorkCar(50, 'black', 'Mercedes', False)
p1 = PoliceCar(90, 'blue', 'Ford', True)

print(f'town car: speed: {t1.speed}, color: {t1.color}, name: {t1.name}, is_police: {t1.is_police}')
t1.go()
t1.stop()
t1.turn('left')
t1.show_speed()

print(f'sport car: speed: {s1.speed}, color: {s1.color}, name: {s1.name}, is_police: {s1.is_police}')
s1.go()
s1.stop()
s1.turn('right')
s1.show_speed()

print(f'work car: speed: {w1.speed}, color: {w1.color}, name: {w1.name}, is_police: {w1.is_police}')
w1.go()
w1.stop()
w1.turn('left')
w1.show_speed()

print(f'police car: speed: {p1.speed}, color: {p1.color}, name: {p1.name}, is_police: {p1.is_police}')
p1.go()
p1.stop()
p1.turn('right')
p1.show_speed()

# Задание 5

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером')

my_pen = Pen('ручка шариковая')
my_pencil = Pencil('карандаш простой')
my_handle = Handle('маркер неоновый')

print(f'my_pen: {my_pen.title}')
my_pen.draw()
print(f'my_pencil: {my_pencil.title}')
my_pencil.draw()
print(f'my_handle: {my_handle.title}')
my_handle.draw()








