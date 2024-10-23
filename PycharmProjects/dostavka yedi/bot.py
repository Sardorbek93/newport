from multiprocessing.connection import address_type

import telebot
import button as bt #с помощью команды  as   можно сокращать
from geopy import Photon

geolocator = Photon(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
) #с Google chrome ищем юсер агент



bot = telebot.TeleBot(token="7490065920:AAHlYu71JYz3JLocrrQuFXK0V9P6SQParWs")

@bot.message_handler(commands=["start"])
def start (message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро пожаловать в бот доставки!")
    bot.send_message(user_id, "Введите своё имя для регистрации")
    bot.register_next_step_handler(message,get_name)
    print(message.text) # отлавливаем слово start который отправил пользователь

def get_name (message):
    user_id = message.from_user.id
    name = message.text
    print(message.text)
    bot.send_message(user_id, "Теперь поделитесь своим номером",
                     reply_markup=bt.phone_button())
    bot.register_next_step_handler(message, get_phone_number, name)

def get_phone_number (message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number #берем номер телефона у пользователя
        print(phone_number)
        bot.send_message(user_id, "Оставьте свою локацию", reply_markup=bt.location_button())
        bot.register_next_step_handler(message, get_location, name, phone_number)
    else:
        bot.send_message(user_id, "Отправьте совй номер через кнопку в меню")
        bot.register_next_step_handler(message, get_phone_number, name)

def get_location (message, name, phone_number):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = geolocator.reverse((latitude, longitude)).address
        print(name, phone_number, address)
        bot.send_message(user_id, "Вы успешно зарегистрировались")
        bot.send_message(user_id, "Главное меню:")
    else:
        bot.send_message(user_id, "Отправьте свою локацию через кнопку в меню")
        bot.register_next_step_handler(message, get_location)



bot.infinity_polling()
