import import_Book as ib
import requests as rq
import insert as ie
import fileview as fv
import csv

def main():
    print('|   Введите пункт меню для действия  |')
    print('--------------------------------------')
    print('|  1: просмотр карточек сотрудников  |')
    print('|  2: изменить карточки сотрудников  |')
    print('|  3: удаление карточек сотрудников  |')
    print('|  4: добавить карточки сотрудников  |')
    print('--------------------------------------')
    choise = input('пункт меню: ')
    if (choise == '1'):
        request = input('Введите тип просмотра карточек(все контакты/по фильтру): ')
        Data = rq.type_of_view(request)
        fv.csv_view(Data)
    elif (choise == '2'):
        ie.insert_book(choise)   
    elif (choise == '3'):
        ie.delete_line(choise)
    elif (choise == '4'):
        ib.new_stuff(choise)
    else:
        print('Error404')
