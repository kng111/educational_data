from telegram.ext.dispatcher import run_async
import requests
import re
import telebot
# 5340502579:AAG6RHH45BCAawxPRFbcYFXuzp4wJGS3eGU
# 5287971365:AAFThBl5HQqkrDiLgdhRPqsAw22jTcGvw5s nry(mb)
bot = telebot.TeleBot('5340502579:AAG6RHH45BCAawxPRFbcYFXuzp4wJGS3eGU')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else: 
        import sqlite3



        db = sqlite3.connect('dr12.db')
        cur = db.cursor()

        def prosmotr_koll1():
            import sqlite3


            db = sqlite3.connect('dr12.db')
            cur = db.cursor()
            cur.execute('SELECT IMY FROM table1')
            result = cur.fetchall()
            Spisok = []
            for i in range(len(result)):
                x = []
                x = result[i]
                l = (''.join(map(str,x)))
                danie = (str(l[:5]))
                Spisok.append(danie)
            return(Spisok)
        def prosmotr_koll2():
            import sqlite3


            db = sqlite3.connect('dr12.db')
            cur = db.cursor()
            cur.execute('SELECT IMY FROM table2')
            result = cur.fetchall()
            Spisok = []
            for i in range(len(result)):
                x = []
                x = result[i]
                l = (''.join(map(str,x)))
                danie = (str(l[:5]))
                Spisok.append(danie)
            return(Spisok)
        def prosmotr_koll3():
            import sqlite3

            db = sqlite3.connect('dr12.db')
            cur = db.cursor()
            cur.execute('SELECT IMY FROM table3')
            result = cur.fetchall()
            Spisok = []
            for i in range(len(result)):
                x = []
                x = result[i]
                l = (''.join(map(str,x)))
                danie = (str(l[:5]))
                Spisok.append(danie)
            return(Spisok)
        def prosmotr_table5():
            cur.execute('SELECT DR FROM table1')
            result = cur.fetchall()
            Spisok = []
            for i in range(len(result)):
                x = []
                x = result[i]
                l = (''.join(map(str,x)))
                danie = (str(l[:5]))
                Spisok.append(danie)
                # print(Spisok)
            return(Spisok)
        # prosmotr_table5()
        def prosmotr_table6():
            cur.execute('SELECT DR FROM table2')
            result = cur.fetchall()
            Spisok = []
            for i in range(len(result)):
                x = []
                x = result[i]
                l = (''.join(map(str,x)))
                danie = (str(l[:5]))
                Spisok.append(danie)
            return(Spisok)
        def prosmotr_table7():
            cur.execute('SELECT DR FROM table3')
            result = cur.fetchall()
            Spisok = []
            for i in range(len(result)):
                x = []
                x = result[i]
                l = (''.join(map(str,x)))
                danie = (str(l[:5]))
                Spisok.append(danie)
            return(Spisok)

        import random


        photo = 'hb.jpg'

        vremy1 = '12:53:30'
        vremy2 = '21:07:40'
        vremy3 = '21:07:50'

        chat_id1 = '-735725249'
        chat_id2 = '-645555348'
        chat_id3 = '-781737930'

        print(chat_id1)


        TOKEN = '5287971365:AAFThBl5HQqkrDiLgdhRPqsAw22jTcGvw5s'
        URL = 'https://api.telegram.org/bot'
        import datetime
        import time
        now = datetime.datetime.now()
        data = str(now.strftime("%m"))
        dr = str(now.strftime("%m"))
        dr = (f'{now.day}/{data}')
	
        def perebor1(dr):
                            cur.execute(f'SELECT IMY FROM table1 WHERE DR = "{dr}"')
                            result = cur.fetchall()
                            list = []
                            for i in range(len(result)):
                                x = result[i]

                                list.append(x)

                            # print(list)
                            list1 = []
                            for i in range(len(list)):
                                x2 = (str(list[i])[2:-3])
                                list1.append(x2)
                            # print(list1)
                            return(list1)
        def perebor2(dr):
                            cur.execute(f'SELECT IMY FROM table2 WHERE DR = "{dr}"')
                            result = cur.fetchall()
                            list = []
                            for i in range(len(result)):
                                x = result[i]

                                list.append(x)

                            # print(list)
                            list1 = []
                            for i in range(len(list)):
                                x2 = (str(list[i])[2:-3])
                                list1.append(x2)
                            # print(list1)
                            return(list1)
        def perebor3(dr):
                            cur.execute(f'SELECT IMY FROM table3 WHERE DR = "{dr}"')
                            result = cur.fetchall()
                            list = []
                            for i in range(len(result)):
                                x = result[i]

                                list.append(x)

                            # print(list)
                            list1 = []
                            for i in range(len(list)):
                                x2 = (str(list[i])[2:-3])
                                list1.append(x2)
                            # print(list1)
                            return(list1)
        def send_photo_file1(chat_id, img,text):
                                    files = {'photo': open(img, 'rb')}
                                    data = {'caption': text}
                                    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files,data=data)
        def send_photo_file2(chat_id, img,text):
                                    files = {'photo': open(img, 'rb')}
                                    data = {'caption': text}
                                    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files,data=data)
        def send_photo_file3(chat_id, img,text):
                                    files = {'photo': open(img, 'rb')}
                                    data = {'caption': text}
                                    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files,data=data)


bot.polling(none_stop=True)

#         def pozdravl():
#                         cur.execute(f'SELECT text FROM table4')
#                         result = cur.fetchall()
#                         list = []
#                         for i in range(len(result)):
#                             x = result[i]

#                             list.append(x)

#                         # print(list)
#                         list1 = []

#                         for i in range(len(list)):
#                             x2 = (str(list[i])[2:-3])
#                             list1.append(x2)
#                         # print(list1)
#                         return(list1)
#         listpozdrav = pozdravl()
#         while True:
#             import sqlite3
          
#             pozdrav = random.choice(listpozdrav)
#             time.sleep(1)
#             now = datetime.datetime.now()
#             vremy = (now.strftime("%H:%M:%S"))
#             print(vremy)
#             data = str(now.strftime("%m"))
#             dr = str(now.strftime("%m"))
#             dr = (f'{now.day}/{data}')
#             for i in range(len(perebor1(dr))):
#                     # print(len(perebor1(dr)))
#                     x =(prosmotr_table5()[i])
#                     imy1 = (perebor1(dr)[i])
#                     if vremy == vremy1:
#                             text = (f'{imy1},{pozdrav}')
#                             send_photo_file1(chat_id1,photo,text)
#                 # -645555348"
            
#             for i in range(len(perebor2(dr))):
#                     x2 =(perebor2(dr)[i])
#                     imy2 = (perebor2(dr)[i])
#                     if vremy ==vremy2:
#                         text = (f'{imy1},{pozdrav}')
#                         send_photo_file2(chat_id2,photo,text)

#             for i in range(len(perebor3(dr))):
#                     x3 =(perebor3(dr)[i])
#                     imy3 = (perebor3(dr)[i])
#                     if vremy == vremy3:
#                         text = (f'{imy1},{pozdrav}')
#                         send_photo_file3(chat_id3,photo,text)
#         # #  -645555348 test 1
# #  -781737930 test 2
# #  -735725249 test 3
# bot.polling(none_stop=True, interval=0)
# # import random

# # mylist = ["apple", "banana", "cherry"]

# # x = (random.choice(mylist))
# # print(x)
# 



# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# print("Бот запущен. Нажмите Ctrl+C для завершения")

# def on_start(update, context):
# 	chat = update.effective_chat
# 	context.bot.send_message(chat_id=chat.id, text="Привет, я Валютный бот")


# def on_message(update, context):
# 	chat = update.effective_chat
# 	text = update.message.text
# 	try:
# 		number = float(text)
# 		rate = 80.34
# 		soms = number * rate
# 		message = "$%.2f = %.2f сом" % (number, soms)
# 		context.bot.send_message(chat_id=chat.id, text=message)
# 	except:
# 		context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")

# token = "5287971365:AAFThBl5HQqkrDiLgdhRPqsAw22jTcGvw5s"

# updater = Updater(token, use_context=True)

# dispatcher = updater.dispatcher
# dispatcher.add_handler(CommandHandler("start", on_start))
# dispatcher.add_handler(MessageHandler(Filters.all, on_message))

# updater.start_polling()
# updater.idle()