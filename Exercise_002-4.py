# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

import random
n = int(input('Enter number of elements: '))
my_list = []
for i in range(1, n + 1):
    my_list.append(random.randint(-n, n))
print(my_list)

position = []
for i in range(1, 3):
    position.append(int(input('Enter number position: ')))

result = my_list[position[0]] * my_list[position[1]]
print(result)
