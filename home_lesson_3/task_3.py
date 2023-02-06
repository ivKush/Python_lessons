# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:

# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

points = 0
for i in input().upper():    
    if (i == 'А' or i == 'В' or i == 'Е' or i == 'И' or i == 'Н' or i == 'О'
            or i == 'Р' or i == 'С' or i == 'Т'):
        points = points + 1
    elif (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'L'
            or i == 'N' or i == 'S' or i == 'T' or i == 'R'):
        points = points + 1
    elif i == 'Д' or i == 'К' or i == 'Л' or i == 'М' or i == 'П' or i == 'У':
        points += 2
    elif i == 'D' or i == 'G':
        points += 2
    elif i == 'Б' or i == 'Г' or i == 'Ё' or i == 'Ь' or i == 'Я':
        points += 3
    elif i == 'B' or i == 'C' or i == 'M' or i == 'P':
        points += 3
    elif i == 'Й' or i == 'Ы':
        points += 4
    elif i == 'F' or i == 'H' or i == 'V' or i == 'W' or i == 'Y':
        points += 4
    elif i == 'Ж' or i == 'З' or i == 'Х' or i == 'Ц' or i == 'Ч':
        points += 5
    elif i == 'K':
        points += 5
    elif i == 'Ш' or i == 'Э' or i == 'Ю':
        points += 8
    elif i == 'J' or i == 'X':
        points += 8
    elif i == 'Ф' or i == 'Щ' or i == 'Ъ':
        points += 10
    elif i == 'Q' or i == 'Z':
        points += 10
print(points)

