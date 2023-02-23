import database


def data_coll():
    print("введите данные: ")
    data = [
        f'{len(database.phone_dir) + 1}',
        input("телефон: "),
        input("фамилия: "),
        input("имя: "),
        input("отчество: ")]
    # return data
    database.phone_dir.append(data)
    # database.phone_dir.insert(len(database.phone_dir), data)
    return database.phone_dir


# database.phone_dir.insert(len(database.phone_dir), data_coll())

# print(data_coll())

# print(database.phone_dir)
