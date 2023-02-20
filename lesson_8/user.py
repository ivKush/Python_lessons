import search_subscriber
import data_collection
import database
# import database_test

# search = search_subscriber.search
# coll = data_collection.data_coll
result = []

select = input(
    "Введите команду: \n(search) - найти абонента \n(coll) - добавить абонента \n(print) - вывести весь справочник \n")

if select == 'search':
    print(*search_subscriber.search(input("Напишите искомые данные: ")))
elif select == 'coll':
    result = data_collection.data_coll()
    database.telephone_directory.append(result)
    
    database_test_1 = open('C:/Python/Python_lessons/lesson_8/database_test.py', 'w+')
    database_test_1.write(str(database.telephone_directory))
    database_test_1.close()
    # print(*database.telephone_directory, sep='\n')
    # database.new_telephone_dir()
elif select == 'print':
    print(*database.telephone_directory, sep="\n")
else:
    print("не верная команда")
    
    