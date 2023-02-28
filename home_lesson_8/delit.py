import database_test


def del_subscriber():
    i = 0
    d = input("Введите id удаляемого абонента: ")
    while i < len(database_test.phone_dir):
        if database_test.phone_dir[i][0] == d:
            database_test.phone_dir.pop(i)
            f = open('home_lesson_8\database_test.py', 'w', encoding='utf-8')
            f.write(f'phone_dir = {database_test.phone_dir}') 
            f.close()
            print("Абонент удален")
            break
        i += 1
    else:
        print('Такого id нет ')
        
            
# del_subscriber()