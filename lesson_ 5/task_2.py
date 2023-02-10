
# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 82

def max_to_min(list):
    min_num = min(list)
    max_num = max(list)
    return [ min_num if i == max_num else i for i in list ]

print(*max_to_min([int(i) for i in input().split()]))
