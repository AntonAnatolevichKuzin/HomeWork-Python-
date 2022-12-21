# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем
# первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

my_list = []
for i in range(1, 8):
    my_list.append(random.randint(0, 10))
print(f'{my_list} => ', end='')

for i in range(len(my_list)):
    if i < (len(my_list)) / 2:
        sum = my_list[i] * my_list[len(my_list) - i - 1]
        print(f'{sum} ', end='')
