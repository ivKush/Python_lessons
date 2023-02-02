# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
# 10 -> 1 2 4 8

num = int(input())
print()
for i in range(num):
    if 2 ** i > num: 
        break
    print(2 ** i)
    
