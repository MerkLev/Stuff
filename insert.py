import csv
import re

def insert_book(data):
    found = False
    with open('book.csv', 'r', encoding='utf-8') as book:
        file_reader = csv.reader(book, delimiter=",", lineterminator="\r")
        buffer_export2 = []
        search_element = input('Введите атрибут поиска = ')
        for line in file_reader:
            buffer_export2.append(line)
        for i in buffer_export2:
            if search_element in i:
                found = True
                buffer_export2.pop(0)
                filtered = list(filter(lambda x: str(search_element) in x, buffer_export2))
                filtered = filtered[0]
                position = buffer_export2.index(filtered)
                data_name = ['id', 'имя','телефон', 'должность']
                for i in range(1, len(data_name)):
                    x = input(f'Введите данные для замены {data_name[i]}= ')
                    filtered[i] = x
                buffer_export2[position] = filtered
                print(f'Текущие данные: {filtered}')
            with open("book.csv","w", encoding='utf-8', newline='') as book:
                file_writer = csv.writer(book, delimiter=",", lineterminator="\r")
                file_writer.writerow(['Ид','имя','телефон','почта'])
                for i in buffer_export2:
                        file_writer.writerow([str(i[0]),str(i[1]),str(i[2]),i[3]])
        if found is False:
            print('Элемент не найден')  


def delete_line(Data):
    found = False
    with open('book.csv', 'r', encoding='utf-8',newline='') as book:
        buffer_export2 = []
        search_element = input('Введите атрибут поиска = ')
        file_reader = csv.reader(book, delimiter=",", lineterminator="\r")
        for row in file_reader:
            buffer_export2.append(row)
        for i in buffer_export2:
            if search_element in i:
                found = True
                buffer_export2.pop(0)
                filtered = list(filter(lambda x: str(search_element) in x, buffer_export2))
                filtered = filtered[0]
                buffer_export2.remove(filtered)
                print(f'удаляемые данные: {filtered}')
                verify = input('Удалить карточку? (да/нет)')
                if (verify == 'да'):
                    with open("book.csv","w", encoding='utf-8', newline='') as book:
                        file_writer = csv.writer(book, delimiter=",", lineterminator="\r")
                        file_writer.writerow(['Ид','имя','телефон','почта'])
                        for i in buffer_export2:
                                file_writer.writerow([str(i[0]),str(i[1]),str(i[2]),i[3]])
        if found is False:
            print('Элемент не найден')