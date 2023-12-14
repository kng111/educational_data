file_path = r'C:\Users\yakvl\Documents\GitHub\educational_data\Bots\Директора\torgovie\group_id.txt'
def orders():
    with open(file_path, 'r', encoding='utf-8') as f:
        list1 = []
        for line in f:
            # Обрабатываем каждую строку (например, выводим ее)
            list1.append(line.strip())  # метод strip() удаляет лишние пробелы и символы перевода строки
        return(list1)

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

def zap(Алроса,Газпром,ЛУКОЙЛ,Магнит,Роснефть,Сбербанк,Совкомфлот,Сургутнефтегаз,Ликвидность):
    with open(r"C:\Users\yakvl\Documents\GitHub\educational_data\Bots\Директора\torgovie\classmates.csv", mode="a", encoding='utf-8') as w_file:
        names = ["Алроса", "Магнит"]
            
        file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                    lineterminator="\r", fieldnames=names)
        file_writer.writerows([{"Алроса": f"{Алроса}","Газпром":f"{Газпром}","ЛУКОЙЛ":f"{ЛУКОЙЛ}","Магнит":f"{Магнит}","Роснефть":f"{Роснефть}","Сбер Банк":f"{Сбербанк}","Совкомфлот":f"{Совкомфлот}","Сургутнефтегаз - привилегированные":f"{Сургутнефтегаз}","ВИМ - Ликвидность":f"{Ликвидность}"}])
