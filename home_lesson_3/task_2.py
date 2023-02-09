# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5
import random
a = []
[a.append(random.randint(-100, 100)) for i in range(1, int(input()) + 1)]
# a = list(range(1, int(input()) + 1))
print(*a)
item = min(a)
min_dif = x = int(input())
if x >= 0:
    for i in a: # для положительных значений
        if x > i:             
            if min_dif > x - i:
                min_dif = x - i
                item = i
        else:
            if min_dif > i - x:
                min_dif = i - x    
                item = i
else:   # для отрицательныых значений
    for i in a:
        if x < i:             
            if min_dif < x - i:
                min_dif = x - i
                item = i
        else:
            if min_dif < i - x:
                min_dif = i - x    
                item = i
print(f'Ближайший элемент: {item}')


# --------Решение от преподавателя------------------------------
from random import randint

list_nums = [randint(1, 21) for _ in range(int(input()))]

print(list_nums)
num = int(input())
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num - right_num):
        right_num = i

print(right_num)