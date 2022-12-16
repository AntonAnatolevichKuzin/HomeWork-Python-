# 5. Реализуйте алгоритм перемешивания списка.

import random

my_list = []
for i in range(1, 8):
    my_list.append(random.randint(-5, 5))
print(my_list)

for i in range(0, len(my_list)):
    if i < len(my_list) - 1:
        temp = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = temp

print(my_list)
