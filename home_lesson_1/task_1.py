# 1. Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

sum = 0
num = input()
for i in num:
   i = int(i)
   sum += i
print(sum)
