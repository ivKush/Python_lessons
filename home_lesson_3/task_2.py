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
[a.append(random.randint(1, 100)) for i in range(1, int(input()) + 1)]
# a = list(range(1, int(input()) + 1))
print(*a)
item = min(a)
min_dif = x = int(input())
for i in a:
    if x > i:             
        if min_dif > x - i:
            min_dif = x - i
            item = i
    else:
        if min_dif > i - x:
            min_dif = i - x    
            item = i
print(f'Ближайший элемент: {item}')

