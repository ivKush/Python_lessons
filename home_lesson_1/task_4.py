# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

size_1 = int(input())
size_2 = int(input())
slice = int(input())

if (slice == (size_1 or size_2) or slice % (size_1 or size_2) == 0 and slice != (size_1 * size_2)):    
    print('yes')
else: 
    print('no')

# m, n, k = int(input()), int(input()), int(input())


