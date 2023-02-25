import search_subscriber
import data_collection
import database   
import txt_dir
from os import path
import database_test
import delit
import change_data
# search = search_subscriber.search
# coll = data_collection.data_coll
# database_test_2 = 'lesson_8\data_test_2.txt'
# select = ''


def menu_command():
    result = []
    start = True
    while start:
        # global select 
        select = input(
        'Введите команду: \n'
        '(1) - найти абонента \n'
        '(2) - добавить абонента \n'
        '(3) - изменение данных абонента \n'
        '(4) - удаление абонента по id\n'
        '(5) - вывести на консоль весь справочник \n'
        '(6) - сохранить справочник в файл txt \n'
        '(7) - выйти из программы \n')
        
        if select == '1':
            # print(*search_subscriber.search(input("Напишите искомые данные: ")), sep='\n')
            search_subscriber.search()
        elif select == '2':
            # Добавляет абонента в database с проверкой на совпадения абонента (без id)
            data_collection.data_coll() 
            
        elif select == '3':
            change_data.edit()

        elif select == '4':
            delit.del_subscriber()      
            # Сделать внутреннее меню для запроса продолжения удаления/возврата в главное меню  
        elif select == '5':
            print(txt_dir.txt_phon_dir(database_test.phone_dir))
            # Добавить выбор сохранения (всё, один, несколько)
        elif select == '6':
            # Сделать запрос на местосохранения файла, вместо указанного (стр. 50)
            f = open('home_lesson_8/database_test.txt', 'w', encoding='utf-8')
            f.write(txt_dir.txt_phon_dir(database_test.phone_dir)) # выводит в файл txt актуальный database
            f.close()
            
        elif select == '7':
            start = False
            
        else:
            print("\nНЕ верная команда \n")
            
menu_command()
