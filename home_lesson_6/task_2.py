'''
ввод
    -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
диапазон
    5
    15
вывод
    [1, 9, 13, 14, 19]
'''
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_1 = list(map(int, input().split()))
num_min = int(input())
num_max = int(input())
# print(list_1)

print([i for i in range(len(list_1)) if num_min <= list_1[i] <= num_max])

# ---------------------- решение преподователя ---------------------------------
# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])
# --------------------------------------------------------------------------------

# i = 0
# list_2 = []
# while i < len(list_1):
#     if list_1[i] >= num_min and list_1[i] <= num_max:
#         # print(list_1[i])
#         list_2.append(i)
#     i +=1
# print(list_2)

