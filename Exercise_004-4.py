# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Input number: '))
print(f'{num} -> ', end='')
binar = ''
while num > 0:
    binar = str(num % 2) + binar
    num = num // 2
print(binar)

