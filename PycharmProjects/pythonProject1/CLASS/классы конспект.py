# class User:   #создавать классы надо с большой буквой.
#     name = 'Admin'  #Обьект
#     password = 12345    #обьект
from html.parser import commentclose


class Car:
    def __init__(self, model, year, color): #Создание пустого класса __init__(self)
        self.car_model = model
        self.car_color = color
        self.car_year = year

nexia = Car (model = "nexia", year  =  1999, color = "white" )
print(nexia.car_year)

class Comment:
    def __init__(self, name, comment, likes = 0):
        self.username = name
        self.text = comment
        self.likes = likes  #Это и есть атрибуты. их можно менять как: #24 cтрока. поменяли 0 на 1
    def delete_comment (self):   #Удаляем комментарию
        print(f'{self.text} комментарий удалился')
    def change_text(self, new_text):
        self.text = new_text + "\nизменено"



bbc = Comment ('goblin', 'kommentariya')
bbc.change_text ("hello") #вверхняя слово 'kommentariya' поменялся на hello

bbc.likes = 1
bbc.username = 'qobil'
print(bbc.likes)
print(bbc.username)
bbc.delete_comment()
print(bbc.text)