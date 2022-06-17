# Задание 1

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        cls.li = date.split('-')
        cls.day = int(cls.li[0])
        cls.month = int(cls.li[1])
        cls.year = int(cls.li[2])
        print(f'day: {cls.day}, month: {cls.month}, year: {cls.year}')

    @staticmethod
    def validate():
        print('day OK') if 1 < Date.day < 31 else print('day should be between 1 and 31')
        print('month OK') if 1 < Date.month < 12 else print('month should be between 1 and 12')
        print('year OK') if Date.year <= 2022 else print('year should not exceed 2022')

print('Задание 1')
date = input('Введите дату в формате дд-мм-гггг: ')
d_1 = Date(date)
d_1.get_date(date)
d_1.validate()
print()


# Задание 2

class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt

print('Задание 2')
try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise ZeroDivError('На ноль делить нельзя!')
except ZeroDivError as err:
    print(err)
else:
    print(f'Результат деления: {a / b}')
finally:
    print('Конец')
    print()

# Задание 3

class NotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

print('Задание 3')
while True:
    el = input('Введите новый элемент списка: ').lower()
    if el == 'stop':
        break
    else:
        try:
            if el.isdigit() == True:
                my_list.append(int(el))
            else:
                raise NotDigit('Это не число')
        except NotDigit as err:
            print(err)
print(my_list)
print()

# Задание 4-6

"""
Проект: Онлайн магазин одежды.

Я создала базовай класс - Товар(Good) - и на его основе классы для отдельных видов товаров: Dress, Shoes и Hat.

В конструктор, созданный на уровне базового класса, на уровне отдельных классов добавляются параметры для размера:
(size_dress, size_shoes, size_hat). Там же создаются разные методы для валидации размеров (для этой цели было создано
исключение WrongSize), а также делается перегрузка печати.

На уровне базового класса созданы все основные методы:
- методы класса:
initiation (инициирует все необходимые мне общие списки и словари),
in_stock_report (выдает словарь с остатками товаров),
sales_report (выдает словарь с общими количествами продаж по товарам)

- методы экземпляра:
receipt (поступление товаров на склад меняет наличие товара, в т.ч. в словаре),
sale (продажа товара меняет наличие товара и количество проданных товаров, в т.ч. в словарях),
available (выдает остаток конкретного товара),
sold (выдает общее количество продаж конкретного товара)

- с помощью геттера и сеттера можно получать и менять цену товаров.
"""

class WrongSize(Exception):
    def __init__(self, txt):
        self.txt = txt

class Good:

    all_goods = []
    goods_in_stock = {}
    total_sales = {}

    @classmethod
    def initiation(cls, name):
        cls.all_goods.append(name)
        my_dict = {name: 0}
        cls.goods_in_stock.update(my_dict)
        cls.total_sales.update(my_dict)

    def __init__(self, description, SKU, material, price):
        self.d = description
        self.SKU = SKU
        self.m = material
        self._p = price
        self.total_receipts = 0
        self.total_sales = 0
        self.in_stock = 0
        Good.initiation(self.d)

    @property
    def price(self):
        print(self._p)

    @price.setter
    def price(self, new):
        self._p = new

    def receipt(self, quantity):
        self.in_stock += quantity
        self.total_receipts += quantity
        my_dict = {self.d: self.in_stock}
        Good.goods_in_stock.update(my_dict)
        print(f'Successful. Received: {quantity}. In stock: {self.in_stock}')

    def sale(self, quantity):
        if quantity <= self.in_stock:
            self.in_stock -= quantity
            self.total_sales += quantity
            my_dict_1 = {self.d: self.in_stock}
            Good.goods_in_stock.update(my_dict_1)
            my_dict_2 = {self.d: self.total_sales}
            Good.total_sales.update(my_dict_2)
            print(f'Successful. Sold: {quantity}. In stock: {self.in_stock}')
        else:
            print(f'Only {self.in_stock} in stock')

    def available(self):
        print(f'Stock of {self.d} (SKU: {self.SKU}) = {self.in_stock}')

    def sold(self):
        print(f'Total sales of {self.d} (SKU: {self.SKU}) = {self.total_sales}')

    @classmethod
    def in_stock_report(cls):
        print(f'Goods in stock: {cls.goods_in_stock}')

    @classmethod
    def sales_report(cls):
        print(f'Goods sold: {cls.total_sales}')


class Dress(Good):
    def __init__(self, description, SKU, material, size_dress, price):
        super().__init__(description, SKU, material, price)
        self.s = size_dress
    def __str__(self):
        return f'Dress. SKU: {self.SKU}, material: {self.m}, size: {self.s}, price: {self._p}'
    def validation(self):
        try:
            if self.s not in [40, 42, 44, 46, 48, 50, 52, 54]:
                raise WrongSize('Dress size should be an even number in range 40-52')
        except WrongSize as err:
            print(err)
        else:
            print('Size OK')


class Shoes(Good):
    def __init__(self, description, SKU, material, size_shoes, price):
        super().__init__(description, SKU, material, price)
        self.s = size_shoes
    def __str__(self):
        return f'Shoes. SKU: {self.SKU}, material: {self.m}, size: {self.s}, price: {self._p}'
    def validation(self):
        try:
            if self.s < 34 or self.s > 44:
                raise WrongSize('Shoes size should be 34-44')
        except WrongSize as err:
            print(err)
        else:
            print('Size OK')


class Hat(Good):
    def __init__(self, description, SKU, material, size_one, price):
        super().__init__(description, SKU, material, price)
        self.s = size_one
    def __str__(self):
        return f'Hat. SKU: {self.SKU}, material: {self.m}, size: {self.s}, price: {self._p}'
    def validation(self):
        try:
            if str(self.s).lower() != 'onesize':
                raise WrongSize('Only OneSize is possible')
        except WrongSize as err:
            print(err)
        else:
            print('Size OK')


d_1 = Dress('dress', 123456, 'silk', 44, 5000)
s_1 = Shoes('shoes', 456234, 'leather', 44, 10000)
h_1 = Hat('hat', 876450, 'wool', 42, 2000)

print('Задание 4-6')
print(d_1)
print(s_1)
print(h_1)
d_1.validation()
s_1.validation()
h_1.validation()
d_1.price
d_1.price = 6000
d_1.price
d_1.receipt(10)
d_1.sale(6)
d_1.available()
d_1.sold()
s_1.receipt(20)
s_1.sale(8)
s_1.available()
s_1.sold()
h_1.receipt(15)
h_1.sale(4)
h_1.available()
h_1.sold()
Good.in_stock_report()
Good.sales_report()
print()

# Задание 7

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'{self.a} + {self.b}i'
    def __add__(self, other):
        summa_a = self.a + other.a
        summa_b = self.b + other.b
        return f'{summa_a} + {summa_b}i'
    def __mul__(self, other):
        el_1 = self.a * other.a - self.b * self.b
        el_2 = self.b * other.a + self.a * other.b
        return f'{el_1} + {el_2}i'

num_1 = ComplexNum(2, 5)
num_2 = ComplexNum(8, 12)

print('Задание 7')
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)
