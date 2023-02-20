import search_subscriber 
import data_collection
import database

# search = search_subscriber.search
# coll = data_collection.data_coll

select = input("Введите команду: \n(search) - найти абонента \n(coll) - добавить абонента \n(print) - вывести весь справочник \n")

if select == 'search':
    print(*search_subscriber.search(input("Напишите искомые данные: ")))
elif select == 'coll': 
    database.telephone_directory.append(data_collection.data_coll())
    print(database.telephone_directory)
elif select == 'print':
    print(database.telephone_directory, sep="\n", end="\n\n")
else:
    print("не верная команда")

