# Задание 1

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))

print(f'Здравствуйте, {name} {surname}! Через 10 лет вам будет {age + 10} лет')

# Задание 2

time = int(input('Введите время в секундах: '))
hours = time // 3600
time_2 = time % 3600
minutes = time_2 // 60
sec = time_2 % 60
print('%02d:%02d:%02d' % (hours, minutes, sec))

# Задание 3

n = input('Введите число: ')
amount = int(n) + int(n * 2) + int(n * 3)
print(amount)

# Задание 4

n = int(input('Введите целое положительное число: '))
max_ = 0
while n > 0:
    n = n // 10
    last = n % 10
    if last > max_:
        max_ = last
print(max_)

# Задание 5

revenue = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))

if revenue > cost:
    profit = revenue - cost
    print(f'Ваша прибыль составляет: {profit}')
    margin = round(profit / revenue * 100)
    print(f'Рентабельность выручки составляет: {margin}%')
    headcount = int(input('Введите численность сотрудников: '))
    profit_per_person = round(profit / headcount)
    print(f'Прибыль на одного сотрудника: {profit_per_person}')
elif revenue < cost:
    loss = cost - revenue
    print(f'Ваш убыток составил: {loss}')
else:
    print("Ваш результат равен нулю")

# Задание 6

a = int(input('Введите дистанцию пробежки за первый день: '))
b = int(input('Введите желаемую дистанцию пробежки: '))
day = 0
while a < b:
    a = a * 1.1
    day += 1
print(f'Вы достигнете желаемого результата ({b} км) на {day} день')









