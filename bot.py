from datetime import datetime as dt # библиотека позволяющая смотреть время
import telebot as tg # библиотека для самого бота в телеграмме
import sysconfig
import sys
import math
import types
class event:
    def __init__(self, text, begin_h, begin_m): # класс для определения времени
        self.text = text # просто объявляем их
        self.begin_h = begin_h
        self.begin_m = begin_m

class user:
    def __init__(self, name, id, kb):
        self.name = name # класс для регистрации, который будет хранить ник, id и группу
        self.id = id
        self.kb = kb



users = []
arr = []
arr.append(event("Подъём - 8:00", 8, 0))
arr.append((event("В 8:30 Зарядка!!!", 8, 30)))
arr.append((event("Завтрак у нас в 9:00", 9, 0)))
arr.append((event("В 9:30 будут мастер-классы", 9, 30)))
arr.append((event("11:00 - у нас коротенький перекус", 11, 0)))
arr.append((event("Вторые мастер-классы начинаются в 11:30", 11, 30)))
arr.append((event("Спортивный час в 13:00", 13, 0)))
arr.append((event("В 2 часа ( или 14:00, как хотите ) у нас обед.", 14, 0)))
arr.append((event("С 15:00 до 16:00 у нас как обычно тихий час, почти как в детском садике :D", 15, 0)))
arr.append((event("Полдник в 16:00 ", 16, 0)))
arr.append((event("16:30 и опять Мастер-классы у нас ", 16, 30)))
arr.append((event("В 18:00 должна быть спортивно-развлекательная программа ( или возможно снова будут занятия :D )", 18, 0)))
arr.append((event("В 19:30 будет ужин",19, 0)))
arr.append((event("Все мероприятия запланированны на 19:30", 19, 30)))
arr.append((event("В 21:30 поздний ужин ввиде быстрой еды, так что я бы сказала, что у тебя целых 25 минут полностью свободного времени", 21, 30)))
arr.append((event("В 22:00 должны все пойти спать...по идее....", 22, 0)))


EGHT = '8:00 - Подъём'
HALFEGT = 'В 8:30 будет зарядка'
NINE = 'В 9:00 у нас завтрак'
HALFNIE = 'В 9:30 начинается первое занятие'
ELLEVEN = '11:00 - короткий перекус'
HALFELLEVEN = '11:30 - второе занятие'
THREETEEN = '13:00 - купаться'
FORTEEN = '14:00 - обееед'
FIVE = '15:00 - наконец-то отдых до 16:00'
FOR = 'На 16:00 запланирован полдник'
HALFFOR = 'В 16:30 продолжаются занятия'
EGHTEEN = '18:00 у нас спортивный часок'
NINETEEN = '19:00 - Ужин'
TWENTY = '21:30 - поздний ужин'
TWELWE = '22:00 - спать, но спать кто-то врятли будет'

def check(current_id): # функция которая проверяет зарегистрирован ли человек
    for i in users:
        if i.id == current_id:
            return 1
    return 0

bot = tg.TeleBot("1871699540:AAG01mW8QuTwN2H9_cGWsdBiHeDH7vi6vOM") # тег бота необходимый для его изменения
@bot.message_handler(commands=['start']) # функция в которой проиходят все действия. commands типо данных( но я могу ошибаться), start - команда в боте для вывода следующего текста
def send_welcome(message):
    bot.reply_to(message, f'Здравствуй, я Айла, приятно с тобой познакомиться, Кохай. Если нужна будет помощь по работе со мной, то просто напиши мне /help и я тебе все объясню, но сначала пройдите регистрацию с помощью команды /reg')


@bot.message_handler(commands=["reg"])
def other_name(message):
    global user_id #глобальная переменная хранящая id зарегистрировшегося пользователя
    user_id = message.from_user.id # принятие информации из текста, который отправляет пользователь
    if check(user_id) == 1: #если такой id уже зарегистрирован, то не дает зарегистрироваться воторой раз
        bot.reply_to(message, f"Ошибка, ты уже прошел регистрацию")
    else:
        bot.reply_to(message, f"Пожалуйста введи свой так называемый в высшем интернете \"ник-нейм\"")

    bot.register_next_step_handler(message, get_name) # переход к следующей функции

def get_name(message):
    global name
    name = message.text.lower() #функция, которая узнает имя пользователя
    bot.reply_to(message, f"Теперь надо чтобы ты написал своё Конструкторское Бюро (проще говоря КБ)")
    bot.register_next_step_handler(message, get_kb)

def get_kb(message):
    global kb
    kb = message.text.lower() #функция, которая узнает группу
    # while not kb == 1:
    if (kb == '1') or (kb == '2') or (kb == '3') or (kb == '4'): # всего 4 кб, если ввести больше или меньше, то регистрация будет отменена и придется проходить её снова
        users.append(user(name, user_id, kb)) #добавление в конец массива user
        bot.reply_to(message, f"Ты зарегистрирован в моей базе данных. Приятного пользования")
        print(users[len(users) - 1].name)
        print(users[len(users) - 1].id) # эти 3 строки чтобы выводить в консоль информацию о зарегистрировавшихся
        print(users[len(users) - 1].kb)
    else:
        bot.reply_to(message, f"Ошибка, в нашем лагере есть от 1 до 4 Конструкторских Бюро\nРегистрация не пройдена, пройди её заново")


@bot.message_handler(commands=['help'])
def send_welcome1(message):
    cur_id = message.from_user.id
    if check(cur_id) == 1: # если данный id не зарегистрирован, то программа не даст ему выполненить дальнейшие команды
        bot.reply_to(message, f'Мои команды: \n' + 'расписание \n' + 'что будет дальше \n' + "что у нас сейчас \n" + "скажи пожалуйста когда спать \n" + "спасибо")
    else:
        bot.send_message(message.from_user.id, "Ошибка, ты не прошел регистрацию. Пожалуйста, сделай это с помощью комманды /reg")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    current_time = dt.now().time() # переменная, котораяя будет проверять текущее время и выводить его ввиде 16 : 18 : 12 : 12312412
    s = message.text.lower() # переменная для считывания текста
    nexttime = current_time.hour
    anoter = current_time.minute
    flag = 0
    cure_id = message.from_user.id
    if check(cure_id) == 1:
        if s == "что у нас сейчас":


            for i in arr:
                eventTime = i.begin_h*100+i.begin_m
                nowTime = nexttime *100 + anoter
                if nowTime > eventTime :
                    s = i.text
            flag = 1
            bot.send_message(message.from_user.id, s)


        if s == "что будет дальше":

            for i in range(len(arr)):
                eventTime = arr[i].begin_h*100+arr[i].begin_m
                nowTime = nexttime *100 + anoter

                if nowTime > eventTime :
                    s = i
            flag = 1
            if s+1 < len(arr):
                bot.send_message(message.from_user.id, arr[s+1].text)




        if s == 'расписание':
            flag = 1
            for i in arr:
                bot.send_message(message.from_user.id, i.text)
            '''bot.send_message(message.from_user.id, EGHT)
            bot.send_message(message.from_user.id, HALFEGT)
            bot.send_message(message.from_user.id, NINE)
            bot.send_message(message.from_user.id, HALFNIE)
            bot.send_message(message.from_user.id, ELLEVEN)
            bot.send_message(message.from_user.id, HALFELLEVEN)
            bot.send_message(message.from_user.id, THREETEEN)
            bot.send_message(message.from_user.id, FORTEEN)
            bot.send_message(message.from_user.id, FIVE)
            bot.send_message(message.from_user.id, FOR)
            bot.send_message(message.from_user.id, HALFFOR)
            bot.send_message(message.from_user.id, EGHTEEN)
            bot.send_message(message.from_user.id, NINETEEN)
            bot.send_message(message.from_user.id, TWENTY)
            bot.send_message(message.from_user.id, TWELWE)'''

        if s == 'скажи пожалуйста когда спать':
            flag = 1
            bot.send_message(message.from_user.id, "По идее спать можно в 22:00 и с 15:00 до 16:00, но ты можешь хоть сейчас")

        if s == 'спасибо':
            flag = 1
            bot.send_message(message.from_user.id, "Всегда пожалуйста.")


        if flag == 0:
            bot.send_message(message.from_user.id, 'Ошибка, я не поняла запроса. Пожалуйста, повторите ещё раз')
    else:
        bot.send_message(message.from_user.id, "Ошибка, ты не зарегистрирован в моей базе данных. Пожалуйста, выполни регистрацию с помощью команды /reg")



bot.polling(none_stop=True)
