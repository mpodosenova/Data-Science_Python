# Задание 2

list_2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list_2 = [list_2[i] for i in range(1, len(list_2)) if list_2[i] > list_2[i-1]]
print(new_list_2)

# Задание 3

list_3 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(list_3)

# Задание 4

list_4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list_4 = [el for el in list_4 if list_4.count(el) == 1]
print(new_list_4)

# Задание 5

from functools import reduce

def summa (a, b):
    return a + b

list_5 = [el for el in range (100, 1001) if el % 2 == 0]
total = reduce(summa, list_5)
print(list_5)
print(total)

# Задание 6

from itertools import count, cycle

def iter_int():
    for a in count(3):
        print(a)
        if a >= 10:
            break

def iter_list(list):
    i = 0
    for b in cycle(list):
        print(b)
        i += 1
        if i >= len(list) * 5:
            break

iter_int()
print()
list = [10, 9, 8]
iter_list(list)

# Задание 7

from math import factorial

def fact(n):
    for i in range (1, n+1):
        yield factorial(i)

for el in fact(5):
    print(el)




