import csv

def csv_view(data):
    found = False
    if (data is True):
        with open("book.csv", 'r', encoding='utf-8') as read_file:
            file_reader = csv.reader(read_file, delimiter=",")
            row_buffer = [row for row in file_reader]
            for i in row_buffer:
                print(i)
    else:
        with open('book.csv', 'r', encoding='utf-8') as book:
            buffer_export2 = []
            search_element = input('Введите данные для фильтрации: ')
            for line in book:
                buffer_export2.append(line)
            for i in buffer_export2:
                if search_element in i:
                    found = True
                    filtered = list(filter(lambda x: str(search_element) in x, buffer_export2))
                    print(filtered)
            if found is False:
                print('Элемент не найден')

