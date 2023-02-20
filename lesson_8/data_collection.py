import database

def data_coll():
    print("введите данные: ")
    data = [
    input("телефон: "),
    input("фамилия: "),
    input("имя: "),
    input("отчество: ")
    ]
    return data

# database.telephone_directory.extend(data_coll())

# print(data_coll())