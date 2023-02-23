import database

def search(arg):
    match = []
    for i in database.phone_dir:
        # for j in range(len(i)):
        for j in i:
            # print(j.upper())
            # if arg == i[j]:
            if arg.upper() == j.upper():
                match.append(i)
    if len(match) == 0: 
        return 'такого абонента нет'
    return match

# print(*search(input()))