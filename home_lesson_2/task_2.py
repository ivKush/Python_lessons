# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
from time import time
import random
# import os
# os.system('cls')

# num_1 = random.randint(1, 1001)
# num_2 = random.randint(1, 1001)

# start = time()

# summ = num_1 + num_2
# mult = num_1 * num_2

# print(f'num_1 = {num_1} \nnum_2 = {num_2}')
# print(f'summa = {summ}')
# print(f'multiplication = {mult}')

# for i in range(1, summ):
#     flag = False
#     for j in range(1, summ):
#         n = i * j
#         if n == mult and i + j == summ:
#             flag = True
#             print(f'{i} \n{j}')
#     if flag == True:
#         break
# print(time() - start)

# from time import time

# 1_000_000_001 1_000_000_000
# s = int(input("Sum of numbers: "))
# p = int(input("The product of numbers: "))
# answer = "I didn't guess."

# start = time()

# d = s ** 2 - 4 * p

# if d >= 0:
#     x_1 = (s + d ** 0.5) // 2
#     x_2 = (s - d ** 0.5) // 2
#     if x_1 * x_2 == p:
#         answer = f"{x_1}, {x_2}"

# print(answer)
# print(time() - start)

# # -------------------- 2 вариант

sum = int(input())
mult = int(input())

start = time()

num_1 = 1
while num_1 < mult:
    num_2 = sum - num_1
    if sum == num_1 + num_2 and mult == num_2 * num_1:
        print(num_1, num_2)
        break
    num_1 += 1
    
print(time() - start)
