# Задача 1. Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9
# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
from random import randint

bot = telebot.TeleBot("5912551029:AAFQjpbDMSwWNvupbX0YLEH8ZVLFWecHvck", parse_mode=None)
count = False
play = False
win_number = 0
steps = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "/play \n/count")


@bot.message_handler(commands=['play'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Давай поиграем я загадал число")
    global play
    global win_number
    play = True
    win_number = randint(1, 1000)


@bot.message_handler(commands=['count'])
def send_welcome(message):
    global count
    count = True
    bot.send_message(message.chat.id, "Введите выражение в формате: 1 + 1 * 1")


@bot.message_handler(content_types=['text'])
def message_listener(message):
    global play
    global count
    global steps
    if play:
        if message.text.isdigit():
            message_number = int(message.text)
            if message_number == win_number:
                play = False
                bot.send_message(message.chat.id,
                                 f'Ты угадал! Загаданное число {win_number}. Ходов: {steps}')
                steps = 0
            elif message_number > win_number:
                steps += 1
                bot.send_message(message.chat.id, 'Меньше')
            elif message_number < win_number:
                steps += 1
                bot.send_message(message.chat.id, 'Больше')
        else:
            print('Введи число')
    elif count:
        message_list = message.text.split()

        result = int(message_list[2]) * int(message_list[4]) + int(message_list[0])
        bot.send_message(message.chat.id, f'Получилось {result}')
        count = False


bot.infinity_polling()
