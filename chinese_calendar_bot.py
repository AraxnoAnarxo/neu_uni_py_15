import telebot
from telebot import apihelper

TOKEN = '991288928:AAGiVU_6Rr3cmNKLNcYcfb8COjtAUxqnQHE'

proxies = {'http': 'http://51.91.212.159:3128',
        'https': 'https://51.91.212.159:3128'

}

apihelper.proxy = proxies

bot = telebot.TeleBot(TOKEN)


# комманда админ
@bot.message_handler(commands = ['admin'])
def admin(message):
    if (message.from_user.username == 'tahoe_ivanova'):
        bot.reply_to(message, 'Салют, Натали!')
    else:
        bot.reply_to(message, 'Ты хто такой.. ээ..')

# комманда help
@bot.message_handler(commands = ['help'])
def help_me(message):
    bot.reply_to(message, 'Мне нечем тебе помочь...')


# комманда start
@bot.message_handler(commands = ['start'])
def what_to_start_with(message):
    bot.reply_to(message, 'Ну и с чего мы начнем?')

# комманда описание (descr)
@bot.message_handler(commands = ['descr'])
def description(message):
    bot.reply_to(message, 'Введи год рождения, и узнаешь, что это за год по Китайскому календарю')

@bot.message_handler(commands = ['commands'])
def all_commands(message):
    bot.reply_to(message, '/admin - для админа\n/help - помощь\n/start - старт\n/descr - описание\n/commands - список всех комманд\n/hello - можешь меня поприветствовать')


# комманда hello

@bot.message_handler(commands=['hello'])
#@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    bot.reply_to(message, 'Очень мило.')

# определить год по китайскому календарю
period = 12

# 1 - козел
goat_list = ['2027']
goat = 2027
for n in range(7):
    goat -= period
    year_str = str(goat)
    goat_list.append(year_str)

# 2 - лошадь
horse_list = ['2026']
horse = 2026
for n in range(7):
    horse -= period
    year_str = str(horse)
    horse_list.append(year_str)

# 3 - змея
snake_list = ['2025']
snake = 2025
for n in range(7):
    snake -= period
    year_str = str(snake)
    snake_list.append(year_str)

# 4 - дракон
dragon_list = ['2024']
dragon = 2024
for n in range(7):
    dragon -= period
    year_str = str(dragon)
    dragon_list.append(year_str)

# 5 - кролик
rabbit_list = ['2023']
rabbit = 2023
for n in range(7):
    rabbit -= period
    year_str = str(rabbit)
    rabbit_list.append(year_str)

# 6 - тигр
tiger_list = ['2022']
tiger = 2022
for n in range(7):
    tiger -= period
    year_str = str(tiger)
    tiger_list.append(year_str)

# 7 - бык
ox_list = ['2021']
ox = 2021
for n in range(7):
    ox -= period
    year_str = str(ox)
    ox_list.append(year_str)

# 8 - крыса
rat_list = ['2020']
rat = 2020
for n in range(7):
    rat -= period
    year_str = str(rat)
    rat_list.append(year_str)

# 9 - свинья
pig_list = ['2019']
pig = 2019
for n in range(7):
    pig -= period
    year_str = str(pig)
    pig_list.append(year_str)

# 10 - собака
dog_list = ['2018']
dog = 2018
for n in range(7):
    dog -= period
    year_str = str(dog)
    dog_list.append(year_str)

# 11 - петух
rooster_list = ['2017']
rooster = 2017
for n in range(7):
    rooster -= period
    year_str = str(rooster)
    rooster_list.append(year_str)

# 12 - обезьяна
monkey_list = ['2016']
monkey_start = 2016
for n in range(7):
    monkey_start -= period
    year_str = str(monkey_start)
    monkey_list.append(year_str)


# текст 4 цифры - определить год по китайскому календарю
@bot.message_handler(regexp=r'\d{4}')
def year_of_birth(message):
#петух 1993
    if message.text in rooster_list:
        bot.reply_to(message, 'Год Петуха')
#собака - 1994
    elif message.text in dog_list:
        bot.reply_to(message, 'Год Собаки')
#свинья - 1995
    elif message.text in pig_list:
        bot.reply_to(message, 'Год Свиньи')
# крыса - 1996
    elif message.text in rat_list:
        bot.reply_to(message, 'Год Крысы')
# бык - 1997
    elif message.text in ox_list:
        bot.reply_to(message, 'Год Быка')
# тигр - 1998
    elif message.text in tiger_list:
        bot.reply_to(message, 'Год Тигра')
# кролик - 1999
    elif message.text in rabbit_list:
        bot.reply_to(message, 'Год Кролика')
# дракон - 2000
    elif message.text in dragon_list:
        bot.reply_to(message, 'Год Дракона')
# змея - 2001
    elif message.text in snake_list:
        bot.reply_to(message, 'Год Змеи')
# лошадь -2002
    elif message.text in horse_list:
        bot.reply_to(message, 'Год Лошади')
# коза - 1991
    elif message.text in goat_list:
        bot.reply_to(message, 'Год Козы')
# обезьяна - 1992
    elif message.text in monkey_list:
        bot.reply_to(message, 'Год Обезьяны')

# https://www.chinahighlights.ru/kakoy-god-kakogo-zhivotnogo/

# текст спокойной ночи
@bot.message_handler(content_types = ['text'])
def good_night(message):
    regex1 = r'{спокойной ночи}'
    regex2 = r'{Спокойной ночи}'
    if (message.from_user.username == 'tahoe_ivanova'):
        if message.text == 'Спокойной ночи':
            bot.reply_to(message, 'Спокойной ночи, дорогая')
    else:
        if message.text in regex1 or message.text in regex2:
            bot.reply_to(message, 'Спокойной ночи!')


# вторая функция с текстом не работает (если переставить местами, работает, то есть работает первая из двух по порядку)
@bot.message_handler(content_types=['text'])
def bot_horoscope(message):
    if message.text == 'Кто ты?':
        bot.reply_to(message, 'Я Дракон')


bot.polling()




