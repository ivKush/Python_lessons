import database
import txt_dir
import database_test

def data_coll():
    flag = True
    while flag:
        print("введите данные: ")
        data = [
            f'{int(database_test.phone_dir[-1][0]) + 1}',
            input("фамилия: "),
            input("имя: "),
            input("отчество: "),
            input("телефон: ")]
        # return data
        i = 0
        while i < len(database_test.phone_dir):
            if len(data[4]) != 12:
                print('Не верно введен номер телефона')
                break
            if data[1:] == database_test.phone_dir[i][1:]:
                print('Данный абонент существует')
                a = input('Желаете выйти? \nДа - 1 \nНет - любой другой символ ')
                if a == '1':
                    flag = False
                    break
                break
            i += 1
        else:            
            database_test.phone_dir.append(data)
            
            f = open('home_lesson_8\database_test.py', 'w', encoding='utf-8')
            # f.write(f'{database_test.phone_dir}') 
            f.write(f'phone_dir = {database_test.phone_dir}') 
            
            # f.write(str(txt_dir.txt_phon_dir(database.phone_dir))) 
            f.close()
            flag = False
        # database.phone_dir.append(data)
        # database.phone_dir.insert(len(database.phone_dir), data)
        # return database.phone_dir
# data_coll()
