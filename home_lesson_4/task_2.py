'''
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

Пример:
4 -> 1 2 3 4
9
'''
import random

bushes = [random.randint(1, 10) for i in range(int(input()))]
print(bushes)
   
for i in range(len(bushes)):
    if i == 0:
        max = bushes[0] + bushes[1] + bushes[-1]
        # max_i = i
    elif i == len(bushes) - 1:
        if max < bushes[-2] + bushes[-1] + bushes[0]:
            max = bushes[-2] + bushes[-1] + bushes[0]
            # max_i = i
    elif bushes[i - 1] + bushes[i] + bushes[i + 1] > max:
        max = bushes[i - 1] + bushes[i] + bushes[i + 1]  
        # max_i = i   
# print(max_i)
print(max)

# ---------------- решение преподователя -----------------------
n = int(input())
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(-1, n - 1):
    bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
    if bush_sum > bush_max:
        bush_max = bush_sum

print(bush_max)

# -------------- хорошее решение студента -------------------------
'''
for i in range(len(N)):
    result_count.append(N[i - 2] + N[i - 1] + N[i])

print(max(result_count))
'''
# -------------------------------------------------------

# bushes = [random.randint(1, 10) for i in range(int(input()))]
# print(bushes)
# # i = 0
   
# for i in range(len(bushes)):
#     if i == 0:
#         max = bushes[0] + bushes[1] + bushes[-1]
#         # max_i = i
#     elif i == len(bushes) - 1:
#         if max < bushes[-2] + bushes[-1] + bushes[0]:
#             max = bushes[-2] + bushes[-1] + bushes[0]
#             # max_i = i
#     elif bushes[i - 1] + bushes[i] + bushes[i + 1] > max:
#         max = bushes[i - 1] + bushes[i] + bushes[i + 1]  
#         # max_i = i   
# # print(max_i)
# print(max)

# while i < len(bushes):
#     if i == 0:
#         max = bushes[0] + bushes[1] + bushes[-1]
#     elif i == len(bushes) - 1:
#         if max < bushes[-2] + bushes[-1] + bushes[0]:
#             max = bushes[-2] + bushes[-1] + bushes[0]
#     elif bushes[i - 1] + bushes[i] + bushes[i + 1] > max:
#         max = bushes[i - 1] + bushes[i] + bushes[i + 1]
#     i +=1
# print(max)


