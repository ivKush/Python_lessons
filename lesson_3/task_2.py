# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

list_nums = [1, 2, 3, 4, 5]
k = 7
print(list_nums)
print()

for i in range(k):
    list_nums.insert(0, list_nums.pop())
    print(f'{i}  {list_nums}')

# result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
# print(result)

1, 2, 3, 4, 5

5, 1, 2, 3, 4   #1
4, 5, 1, 2, 3   #2
3, 4, 5, 1, 2   #3
2, 3, 4, 5, 1   #4
1, 2, 3, 4, 5   #5
5, 1, 2, 3, 4   #6
4, 5, 1, 2, 3   #7


# def swap_1(lst, k):
#     if k < 0:
#         for i in range(abs(k)):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(k):
#             lst.insert(0, lst.pop())
#     return lst 


# lst = [int(input(f"Введите {i + 1}-ое число: ")) for i in range(int(input("Введите размерность списка: ")))]
# print(swap_1(lst, int(input("Введите значение сдвига вправо: "))))