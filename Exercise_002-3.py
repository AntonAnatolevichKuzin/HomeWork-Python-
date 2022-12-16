# 3 Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

n = int(input('Enter number N: '))
my_dict = {}
res_sum = 0
for i in range(1, n + 1):
    my_dict[i] = round((1 + 1/i) ** i, 3)
    res_sum += my_dict[i]
print(f'From n = {n}: {my_dict}')
print(f'Sum = {res_sum}')
