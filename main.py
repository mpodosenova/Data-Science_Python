# Задание 1

''' Я не понимаю, как можно сделать этот код более универсальным, поэтому написала его для матриц 3 на 3'''

class Matrix:

    def __init__(self, matrix):
        self.m = matrix

    def __str__(self):
        list_m = []
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                list_m.append(self.m[i][j])
        l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9 = list_m
        return f'{l_1:<2} {l_2:<2} {l_3:<2} \n{l_4:<2} {l_5:<2} {l_6:<2} \n{l_7:<2} {l_8:<2} {l_9:<2}'

    def __add__(self, other):
        new_m = [[], [], []]
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                summa = self.m[i][j] + other.m[i][j]
                new_m[i].append(summa)
        return Matrix(new_m)

a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[5, 6, 7], [8, 9, 10], [11, 12, 13]])

print(a)
print()
print(b)
print()
print(a + b)

# Задание 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new):
        self._size = new

    @abstractmethod
    def fabric(self):
        pass

class Coat(Clothes):
    @property
    def fabric(self):
        return round(self._size / 6.5 + 0.5, 1)

class Suit(Clothes):
    @property
    def fabric(self):
        return round(2 * self._size + 0.3, 1)

coat_1 = Coat(50)
print(f'Размер пальто: {coat_1.size}')
print(f'Расход ткани на пальто: {coat_1.fabric} м')
coat_1.size = 52
print(f'Новый размер пальто: {coat_1.size}')
print(f'Новый расход ткани на пальто: {coat_1.fabric} м')
print()
suit_1 = Suit(180)
print(f'Ростовка костюма: {suit_1.size} см')
print(f'Расход ткани на костюм: {suit_1.fabric} м')
coat_1.size = 175
print(f'Новая ростовка костюма: {suit_1.size} см')
print(f'Новый расход ткани на костюм: {suit_1.fabric} м')

# Задание 3

class Cell:
    def __init__(self, particles):
        self.p = particles

    def __str__(self):
        return f'{self.p}'

    def __add__(self, other):
        return self.p + other.p

    def __sub__(self, other):
        if self.p > other.p:
            return self.p - other.p
        else:
            return 'Разность отрицательна'

    def __mul__(self, other):
        return self.p * other.p

    def __truediv__(self, other):
        return self.p // other.p

    def make_order(self, num_in_row):
        rows = self.p // num_in_row
        el = '*' * num_in_row
        el_last = '*' * (self.p % num_in_row)
        li = []
        if self.p % num_in_row == 0:
            for i in range(rows):
                li.append(el)
            return '\n'.join(li)
        else:
            for i in range(rows):
                li.append(el)
            li.append(el_last)
            return '\n'.join(li)

cell_1 = Cell(20)
cell_2 = Cell(12)

print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print()
print(cell_2.make_order(5))