# import requests
# from bs4 import BeautifulSoup

# from ordes_W import orders

# def name1(url):
#     response = requests.get(url)


#     from requests_html import HTMLSession

#     session = HTMLSession()
#     response = session.get(url)


#     from bs4 import BeautifulSoup


#     html_content = response.content  

#     # Создаем объект BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Находим элемент span с указанным классом
#     name_span = soup.find('span', {'class': 'SecurityHeader__showName_iw6qC'})

#     # Извлекаем текстовое содержимое элемента
#     if name_span:
#         name = name_span.text.strip()
#         print(f"Название: {name}")
#     else:
#         print("Элемент не найден.")


# data_ordes = orders()
# # Пройдемся по элементам списка и выведем их
# for item in data_ordes:

    
#     price = name1(item)

import csv
def read():
    with open(r"C:\Users\yakvl\Documents\GitHub\educational_data\Bots\Директора\torgovie\classmates.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                # Вывод строк
                print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
            count += 1
        print(f'Всего в файле {count} строк.')




from collections import OrderedDict
from newbot import get_stock_price
from ordes_W import orders
def zap(*args):
    with open(r"C:\Users\yakvl\Documents\GitHub\educational_data\Bots\Директора\torgovie\classmates.csv", mode="a", encoding='utf-8') as w_file:
        names = ["Алроса", "Газпром", "ЛУКОЙЛ", "Магнит", "Роснефть", "Сбер Банк", "Совкомфлот", "Сургутнефтегаз - привилегированные", "ВИМ - Ликвидность","Дата"]
        
        # Упорядочиваем аргументы в соответствии с порядком полей
        ordered_args = [args[names.index(name)] for name in names]
        
        # Используем OrderedDict для сохранения порядка полей
        row_dict = OrderedDict(zip(names, ordered_args))
        
        file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=names)
        file_writer.writerow(row_dict)

# Пример использования

from datetime import datetime
import time
for i in range(10):
    

    # Получите текущую дату и время
    сегодня = datetime.now()

    # Выведите сегодняшнюю дату и день недели

    date = [сегодня.strftime("%d/%m/%H:%M|%A")]
    
    def zxc(date): # 3 Секунды
        data_ordes = orders()
        price = []
        for item in data_ordes:

            # names = name1(item)
            price.append(get_stock_price(item))
        price.extend(date)
        zap(*price)

    start_time = time.time()
    zxc(date)
    end_time = time.time()

    # Выводим время выполнения
    execution_time = end_time - start_time
    print(f"Время выполнения функции: {execution_time} секунд")