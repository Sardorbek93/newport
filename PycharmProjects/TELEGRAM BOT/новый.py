# перед начало в терминале пишем pip install telebot
import telebot

token = "8161501762:AAFtMuM040h1rDb3pYn2aOhJoXx0g2LTYvU"
# создаем обьект бота
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=["start", "help"]) #декоратор для вызова команды
def start(message):
    user_id = message.from_user.id
    name = message.from_user.username
    print(message)
    bot.send_message(user_id, f'Привет {name}')
    bot.send_message(user_id, "HALLO")



@bot.message_handler(content_types=["text"])
def text(message):
    user_id = message.from_user.id
    user_text = message.text
    bot.send_message(user_id, user_text)

@bot.message_handler(content_types=["text"])
def text(message):
    user_id = message.from_user.id
    user_text = message.text
    if user_text.lower() == 'Prognoz':
        bot.send_message(user_id, '+5,+9')
    else:
        bot.send_message(user_id, user_text)


bot.infinity_polling() #создаем команду для бесконечной Работы бота
#bot.polling (non_stop = True) #второй вариант для бесконечной работы бота
