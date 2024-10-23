# перед начало в терминале пишем pip install telebot
import telebot
import buttons


token = "8161501762:AAFtMuM040h1rDb3pYn2aOhJoXx0g2LTYvU"
# создаем обьект бота
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=["start", "help"]) #декоратор для вызова команды
def start(message):
    user_id = message.from_user.id
    name = message.from_user.username
    print(message)
    bot.send_message(user_id, f'Привет {name}', reply_markup=buttons.main_menu())
    bot.send_message(user_id, "HALLO")



@bot.message_handler(content_types=["text"])
def text(message):
    user_id = message.from_user.id
    user_text = message.text
    if user_text.lower() == "prognoz":
        bot.send_message(user_id, "+5,+9")
    elif user_text.lower()== "prognoz na zavtra":
        bot.send_message(user.id, "+10,+15" )
    else:
        bot.send_message(user_id, "Я вас не понял")


bot.infinity_polling() #создаем команду для бесконечной Работы бота
#bot.polling (non_stop = True) #второй вариант для бесконечной работы бота

