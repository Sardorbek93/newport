# def say_hello(): #Создаем функцию
#     print("hello world") #созданная функция
#     print("see") #созданная фукнция
#     print("go") #созданная функция
# say_hello() # при наборе функции показывает 3 printa
# say_hello()
#
#
# #RETURN - позволяет написать что угодно в лист
# def create_list():
#     my_list = []
#     return "Функция успешно выполнена" #Без ретурна невозможна добавить символы, арифметика и т.д.
# a = create_list()
# print(a)

def percent (num, per):
    return (num * per) / 100
print(percent(1800,20))

def spam1 (**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        return f" {k} {v}"
print(spam1(name = 'my1', age = 23))

