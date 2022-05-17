# Задание 1

li = ['text', 123, 6.5, True, [1, 2, 3]]

for element in li:
    print(f'Элемент {element} имеет тип {type(element)}')

# Задание 2

li = list(input('Введите числа: '))

for i in range(0, len(li) - 1, 2):
    li[i], li[i + 1] = li[i + 1], li[i]
print(li)

# Задание 3 (решение через dict)

month = int(input('Ведите номер месяца: '))
months = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for i in months:
    if month in months[i]:
        print(f'Месяц {month} - это {i}')

# Задание 3 (решение через list)

months_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
month_ = int(input('Ведите номер месяца: '))
index_ = months_list.index(month_)
if 0 <= index_ <= 2:
    season = 'зима'
elif 3 <= index_ <= 5:
    season = 'весна'
elif 6 <= index_ <= 8:
    season = 'лето'
elif 9 <= index_ <= 11:
    season = 'осень'
print(f'Месяц {month_} - это {season}')


# Задание 4

st = input('Введите строку из нескольких слов: ')
li = st.split()
for i, n in enumerate(li, 1):
    if len(n) > 10:
        print(i, n[0:10])
    else:
        print(i, n)

# Задание 5

my_list = [7, 5, 3, 3, 2]

max_el = max(my_list)
max_ind = my_list.index(max_el)
min_el = min(my_list)
min_ind = my_list.index(min_el)

n = int(input('Введите цифру: '))

if n > max_el:
    my_list.insert(max_ind, n)
elif n < min_el:
    my_list.insert(min_ind + 1, n)
elif n in my_list:
    my_list.insert(my_list.index(n) + 1, n)

print(my_list)

# Задание 6

list_dict = []
list_names = []
list_prices = []
list_quantities = []
list_units = []
i = 1

while True:
    cond = input("Внести новый товар в базу данных? ").lower()
    if cond == "да":
        name = input('Введите название товара: ')
        price = int(input('Введите цену товара: '))
        quantity = int(input('Введите количество товара: '))
        unit = input('Введите единицу измерения: ')
        new_dict = dict(название=name, цена=price, количество=quantity, ед=unit)
        list_dict.append((i, new_dict))
        i += 1
        list_names.append(name)
        list_prices.append(price)
        list_quantities.append(quantity)
        list_units.append(unit)
    else:
        break
print(list_dict)
my_dict = dict(название=list_names, цена=list_prices, количество=list_quantities, ед=list(set(list_units)))
print(my_dict)