import requests
from bs4 import BeautifulSoup

import ordes_W
def get_stock_price(url):
    try:

        response = requests.get(url)


        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')



            money_span = soup.find('span', {'class': 'Money-module__money_p_VHJ', 'data-qa-type': 'uikit/money'})
            
            


            # Извлекаем значения
            if money_span:
                # Объединяем текстовые узлы и удаляем неразрывные пробелы
                value = ''.join(money_span.stripped_strings)
                return value
            else:
                print("Элемент не найден.")




        else:
            print(f"Ошибка {response.status_code}")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Пример использования





import requests
from bs4 import BeautifulSoup



def name1(url):
    response = requests.get(url)


    from requests_html import HTMLSession

    session = HTMLSession()
    response = session.get(url)


    from bs4 import BeautifulSoup


    html_content = response.content  

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Находим элемент span с указанным классом
    name_span = soup.find('span', {'class': 'SecurityHeader__showName_iw6qC'})

    # Извлекаем текстовое содержимое элемента
    if name_span:
        name = name_span.text.strip()
        print(f"{name}")
    else:
        print("Элемент не найден.")


data_ordes = ordes_W.orders()
# Пройдемся по элементам списка и выведем их















# Пройдемся по элементам списка и выведем их

    
# if price is not None:
#     print(f"Цена акций ALRS: {price}")
# else:
#     print("Не удалось получить цену акций.")

