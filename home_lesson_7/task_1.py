'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке

Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
Вывод: Парам пам-пам
'''
char = 'аеуояиюыэё'

a = len(set([i.count(j) for i in input().split() for j in char if j in i]))
if a == 1: print('Парам пам-пам')
else: print('Пам парам')


# quantity = []
# a = [(input().split())]
# # print(a)
# for i in a[0]:
#     for j in char:
#         if j in i:
#             quantity.append(i.count(j))

# print(quantity)
# if len(set(quantity)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
