# 1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

a = []
[a.append(i) for i in range(1, int(input()) + 1)]
print(*a)
print(a.count(int(input())))

# --------Решение от преподавателя--------------------------------------
list_nums = [int(input()) for _ in range(int(input()))]
print(list_nums.count(int(input())))

# a = []
# for i in range(1, int(input()) + 1):
#     a.append(i)
# print(*a)
# # x = int(input())
# print(a.count(int(input())))



