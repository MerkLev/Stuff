import csv

def get_id():
    with open('book.csv', 'r', encoding='utf-8') as book:
        file_reader = csv.reader(book, delimiter = ",")
        data =[row for row in file_reader]
        buffer =  data[-1]
        id = buffer[0]
    return(int(id) + 1)


def new_stuff(data):
    with open("book.csv", mode="a", encoding='utf-8', newline='') as book:
        file_writer = csv.writer(book, delimiter=",", lineterminator="\r")
        count = int(input('Укажите количество новых сотрудников: '))
        for i in range(0, count):
            new_line = [(int(get_id())+ i), input('Имя = '), input('Телефон = '), input('Должность = ')]
            file_writer.writerow(new_line)