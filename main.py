# Задание 1

f = open('text_1.txt', 'x', encoding='utf-8')

while True:
    a = input('Введите данные: ')
    f.write(a)
    f.write('\n')
    if not a:
        break

f.close()

# Задание 2

with open('text_2.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    print(text)
    rows = len(text)
    print(f'Количество строк: {rows}')
    for i in range(rows):
        words = len(text[i].split())
        print(f'Количество слов в строке {i+1}: {words}')

# Задание 3

with open('text_3.txt', 'r', encoding='utf-8') as f:
    list_1 = f.readlines()

    list_2 = []
    for el in list_1:
        el_new = el[:-1].split()
        list_2.append(el_new)

    for i in range(len(list_2)):
        list_2[i][1] = int(list_2[i][1])

    list_values = []
    low_list = []
    for el in list_2:
        list_values.append(el[1])
        if el[1] < 20000:
            low_list.append(el[0])
    average = sum(list_values) / len(list_values)

    print(f'Сотрудники с окладом менее 20,000 руб: {(", ").join(low_list)}')
    print(f'Средняя величина дохода сотрудников: {average} руб.')

# Задание 4

f_4 = open('text_4.txt', 'r', encoding='utf-8')
f_4_new = open('text_4_new.txt', 'a', encoding='utf-8')

text = f_4.readlines()
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for i in range(len(text)):
    li = text[i].split()
    n = li.pop(0)
    li.insert(0, my_dict.get(n))
    li.append('\n')
    line = ' '.join(li)
    f_4_new.write(line)

f_4.close()
f_4_new.close()

# Задание 5

f_5 = open('text_5.txt', 'r+', encoding='utf-8')

nums = input('Введите числа через пробел: ')
f_5.write(nums)
f_5.seek(0)
text = f_5.read()
list = list(map(int, text.split()))
summa = sum(list)
print(f'Сумма чисел: {summa}')

f_5.close()

# Задание 6

with open('text_6.txt', 'r', encoding='utf-8') as f_6:
    text = f_6.readlines()
    list_from_file = []
    for el in text:
        text_2 = el.split()
        list_from_file.append(text_2)
    print(list_from_file)

    keys = []
    for i in range(len(list_from_file)):
        n = list_from_file[i][0].replace(':', '')
        keys.append(n)

    total_list = []
    for el in list_from_file:
        lists = []
        for item in el:
            digits = []
            for letter in item:
                try:
                    digit = str(int(letter))
                    digits.append(digit)
                except ValueError:
                    pass
            a = ''.join(digits)
            lists.append(a)
        total_list.append(lists)
    print(total_list)

    values = []
    for el in total_list:
        summa = 0
        for digit in el:
            try:
                summa += int(digit)
            except ValueError:
                pass
        values.append(summa)
    print(values)

    my_dict = {}
    for i in range(len(values)):
        new_dict = {keys[i]: values[i]}
        my_dict.update(new_dict)
    print(my_dict)

# Задание 7

import json

with open('text_7.txt', 'r', encoding='utf-8') as f_7:
    text = f_7.readlines()
    list = []
    for el in text:
        list.append(el.split())

    firms = []
    profits = []
    positive_profit = []
    total_revenue = 0
    total_costs = 0
    for el in list:
        firms.append(el[0])
        revenue = int(el[2])
        total_revenue += revenue
        costs = int(el[3])
        total_costs += costs
        profit = revenue - costs
        profits.append(profit)
        if profit > 0:
            positive_profit.append(profit)

    average_profit = round(sum(positive_profit) / len(positive_profit), 1)

    final_list = []
    main_dict = {}
    for i in range(len(firms)):
        new_dict = {firms[i]: profits[i]}
        main_dict.update(new_dict)
    final_list.append(main_dict)
    average_dict = {'average_profit': average_profit}
    final_list.append(average_dict)
    print(final_list)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(final_list, f)