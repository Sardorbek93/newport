from telebot import types

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Создаем кнопки
    button1 = types.KeyboardButton(text="Prognoz")
    button2 = types.KeyboardButton(text="Prognoz na zavtra")

# Добавляем кнопку в пространстве
    kb.add(button1, button2)
    return kb


