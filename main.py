# Задание 1

def division(arg_1, arg_2):
    try:
        n = arg_1 / arg_2
        print(n)
    except ZeroDivisionError:
        print('На ноль делить нельзя')

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

division(a, b)

# Задание 2

def func(name, surname, year, city, email, phone):
    print(f'Данные пользователя: {name} {surname}, год рождения: {year}, город проживания: {city}, почта: {email}, телефон: {phone}')

name_1 = input('Введите имя: ')
surname_1 = input('Введите фамилию: ')
year_1 = input('Введите год рождения: ')
city_1 = input('Введите город проживания: ')
email_1 = input('Введите адрес электронной почты: ')
phone_1 = input('Введите телефон: ')

func(name=name_1, surname=surname_1, year=year_1, city=city_1, email=email_1, phone=phone_1)

# Задание 3

def my_func(*args):
    li = []
    a = int(input('Введите первое число: '))
    li.append(a)
    b = int(input('Введите второе число: '))
    li.append(b)
    c = int(input('Введите третье число: '))
    li.append(c)
    min_digit = min(li)
    li.remove(min_digit)
    print(sum(li))

my_func()

# Задание 4, вариант 1

def my_func(x, y):
   return x ** y

x = int(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))

print(my_func(x, y))

# Задание 4, вариант 2

def my_func(x, y):
   result = 1
   for i in range(-y):
       result /= x
   print(result)

x = int(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))

my_func(x, y)

# Задание 5 (специальный символ для остановки программы - &)

def my_func(*args):
    total_list = []
    while True:
        li = input('Введите числа через пробел: ').split()
        for el in li:
            if el == '&':
                print(sum(total_list))
                print("Stop")
                return
            else:
                total_list.append(int(el))
        print(sum(total_list))

my_func()

# Задание 6

def int_func(n):
    return n.title()

print(int_func('text'))

# Задание 7

def int_func(n):
    return n.title()

n = input('Введите строку из нескольких слов: ')
print(int_func(n))




