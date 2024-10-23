#Lambda функция - это функция программировния в одну строчку.
from urllib3 import proxy_from_url

result = lambda a,b: (a+b)/2
print(result(2,50))
#
# def percent (num, per):            #Обычний код
#     return (num * per) / 100
# print(percent(1800,20))

percent = lambda a,b: (a*b)/100 # создаем переменную и формулу в один строк с функцией LAMBDA
print(percent(1000,10))   # выводим результат






#  map() - встроенная функция в Python, которая принимает 2 аргумента (функция (чаще всего Lambda),
# итерируемый обьект (str, list, tuple, dict)
# функци передаваемая в агрумент будет вЫполнятся для каждого элемента итерируемого обьекта

        # ФУНКЦИЯ MAP равень цикл for
list1 = [1000, 1500, 2000, 5000, 10000] #одна строчка
print(list(map(lambda a: a * 10 / 100, list1 )))

list2 = []  #Код в три строчка.
for a in list1:
    list2.append(a * 10 / 100)
print(list2)


#             filter ()    -   ФИЛЬТР/ встроенная


# list1 = ["ivan", "jabbar", "gamer", "gurik"]
# print(list(filter(lambda a, "a" in a.lower, list1 ()))



x = [1,2,-4,-8,-7,4,18,19,21,-98,]
y = filter(lambda number: number > 0, x )  #lambda number: number >0, x -- sozdayem peremennuyu kotoroe popadaet number > 0 s lista X
print(list(y))

z = map(lambda )