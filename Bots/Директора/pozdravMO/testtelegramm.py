import random
import requests
import sqlite3
import datetime
import time
import logging

TOKEN = '123'
URL = 'https://api.telegram.org/bot'


chat_id1 = -735725249

vremy1 = '01:14:00'

logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_database(database_path):
    return sqlite3.connect(database_path)

def close_database_connection(connection):
    connection.close()

def send_message(chat_id, text):
    data = {'text': text}
    requests.post(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}', data=data)

def get_birthday_greeting(name):
    greetings = [
    f'\U0001F47E: {name}, с днём рождения! Желаю вам дней полных света, счастья и радости. Пусть каждый момент приносит удовлетворение и новые впечатления! \U0001F389',
    f'\U0001F47E: Поздравляю с важным событием - днём рождения, {name}! Пусть в этот день вас окружают близкие и любимые люди, а годы жизни принесут только благополучие и успехи. \U0001F389',
    f'\U0001F47E: С днём рождения, {name}! Пусть этот год будет наполнен яркими моментами, интересными встречами и приятными сюрпризами. Желаю вам всяческого благополучия! \U0001F389',
    f'\U0001F47E: Поздравляю с днём рождения, {name}! Пусть каждый день будет полон смысла и радости, а каждый шаг приводит к исполнению мечтаний. \U0001F389',
    f'\U0001F47E: Специально для вас в этот особенный день: пожелания здоровья, счастья, любви и удачи, {name}! Поздравляю с днём рождения! \U0001F389',
    f'\U0001F47E: Поздравляю с этим радостным днём, {name}! Желаю, чтобы все ваши планы сбылись, а впереди вас ждали только светлые перспективы. \U0001F389',
    f'\U0001F47E: Счастья, радости, тепла и любви в ваш день рождения, {name}! Пусть новый год жизни приносит вам только хорошее! \U0001F389',
    f'\U0001F47E: С днём рождения, {name}! Пусть этот день станет началом новых, ярких путей и запоминающихся моментов в вашей жизни. \U0001F389',
    f'\U0001F47E: С днём рождения, {name}! Желаю вам ярких событий, интересных встреч и счастливых мгновений. Пусть ваше сердце наполняется радостью! \U0001F389',
    f'\U0001F47E: Поздравляю с днём рождения, {name}! Пусть этот день принесет много радости и улыбок. Желаю ярких эмоций и вдохновения! \U0001F389',
    f'\U0001F47E: С днём рождения, {name}! Пусть в этот особенный день сбудется все, о чём вы мечтали. Здоровья, радости и удачи! \U0001F389'
]
    return random.choice(greetings)

def main():
    db = connect_to_database(r'drMO2.db')
    cur = db.cursor()

    while True:
        try:
            now = datetime.datetime.now()
            vremy = now.strftime("%H:%M:%S")
            dr = f'{now.day}/{now.month}'

            cur.execute(f'SELECT imy FROM table1 WHERE DR = "{dr}"')
            result = cur.fetchall()

            for row in result:
                name = row[0]
                if vremy == vremy1:
                    greeting = get_birthday_greeting(name)
                    send_message(chat_id1, greeting)

            time.sleep(1)

        except Exception as e:
            logging.error(f'Error: {e}')
            print(f'Error: {e}')

    close_database_connection(db)

if __name__ == '__main__':
    print('bot start'),main()
