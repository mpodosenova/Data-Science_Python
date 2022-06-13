# Задание 1

from sys import argv

def salary(hours, rate, bonus):
    return (hours * rate) + bonus

hours, rate, bonus = map(int, argv[1:])

print(salary(hours, rate, bonus))