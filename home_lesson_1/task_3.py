# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# ticket = input()
# if len(ticket) != 6:
#     print("неверно ввели номер билета")
# else:
#     sum_1 = 0
#     sum_2 = 0
#     for i in ticket[:3]:
#         # i = int(i)
#         sum_1 += int(i) 
#     for i in ticket[-3:]:
#         # i = int(i)
#         sum_2 += int(i)
#     if sum_1 == sum_2:
#         print("это счастливый билет!!!")
#     else:
#         print("это НЕ счатливый билет :( ")    


# num_1 = [int(i) for i in ticket[0: 3]]
# for i in num_1:
#     sum_1 = i + sum_1
# num_2 = [int(i) for i in ticket[-3:]]
# for i in num_2:
#     sum_2 = i + sum_2
# if sum_1 == sum_2:
#     print("это счастливый билет!!!")
# else:
#     print("это НЕ счатливый билет :( ")
    
# n = (input('bilet number: '))
# total1, total2 = 0, 0
# for i in n[:len(n) // 2]:
#     total1 += int(i)
# for j in n[len(n) // 2:]:
#     total2 += int(j)
# if total1 == total2:
#     print('happy!')
# else: print('dont happy')
s = input()    
p = int(input())
m = float(input())
c = int(input())
sum = p * m
if c >= sum:
    print("Чек")
    print(f'{s} - {m} кг - {p} руб/кг')
    print(f'Итого: {sum} руб')
    print(f'Внесено: {c} руб')
    print(f'Сдача: {c - sum} руб')
    
else:
    print("у вас не хватает денег")
    
   
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(a - int(38 * 2.5))

      
# a = int(input())
# print(a - 38)