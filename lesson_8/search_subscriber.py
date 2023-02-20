import database

def search(arg):
    match = []
    for i in database.telephone_directory:
        # for j in range(len(i)):
        for j in i:
            # print(j.upper())
            # if arg == i[j]:
            if arg.upper() == j.upper():
                match.append(i)
    if len(match) == 0: 
        return 'no subscriber'
    return match

# print(*search(input()))