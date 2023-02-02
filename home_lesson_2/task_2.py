# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import random
import os
os.system('cls')

num_1 = random.randint(1,1001)
num_2 = random.randint(1,1001)

summ = num_1 + num_2
mult = num_1 * num_2

print(f'num_1 = {num_1} \nnum_2 = {num_2}')
print(f'summa = {summ}')
print(f'multiplication = {mult}')

for i in range(summ + 1):
    flag = False
    for j in range(summ + 1):
        n = i * j
        if n == mult and i + j == summ: 
            flag = True
            print(f'{i} \n{j}')            
    if flag == True:
        break
 
    
       

