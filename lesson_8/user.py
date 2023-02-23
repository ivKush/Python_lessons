import search_subscriber
import data_collection
import database   
import export_dir
from os import path
import database_test

# search = search_subscriber.search
# coll = data_collection.data_coll
result = []
database_test_2 = 'lesson_8\data_test_2.txt'
select = ''


def menu_command():
    start = True
    while start:
        # global select 
        select = input(
        'Введите команду: \n'
        '(1) - найти абонента \n'
        '(2) - добавить абонента \n'
        '(3) - изменение данных абонента \n'
        '(4) - удаление абонента \n'
        '(5) - вывести весь справочник \n'
        '(6) - сохранить справочник в файл \n'
        '(7) - выйти из программы \n')
        
        if select == '1':
            print(*search_subscriber.search(input("Напишите искомые данные: ")), sep='\n')
        elif select == '2':
            result = data_collection.data_coll() # возвращает список с добавленным абонентом
            # print(result)
            
            # with open('lesson_8\database_test.py', "a", encoding="utf-8") as f:
            #     f.write(database.phone_dir.append(result))
            
        elif select == '3':
            pass

        elif select == '4':
            pass        
        elif select == '5':
            print(export_dir.export_phon_dir(database.phone_dir))
            
        elif select == '6':
            f = open(
                'C:/Python/Python_lessons/lesson_8/database_test.txt', 'a', encoding='utf-8')
            f.write(export_dir.export_phon_dir(result)) # выводит в файл, только после добавления абонента, нужно добавить выбор от куда выводить (result)
            f.close()
            
        elif select == '7':
            start = False
            
        else:
            print("\nНЕ верная команда \n")
            
    

menu_command()
