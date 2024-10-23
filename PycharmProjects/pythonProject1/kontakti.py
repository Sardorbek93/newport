#contact - в приложение должно присутствовать удаление, изменение, добавление контактов
from operator import index

names = ["Father", "Mother", "Brother", "Sister", "Wife"]
numbers = ["991234567", "978765432", "937654321","900123456", "919876543"]
#sprashivayu imya polzovatelya
username = input("Введите ваше имя пожалуйста:")
info_contact = input (f'Приветствую {username}. Выберите пункт пожалуйста: добавить, изменить, удалить')
#sparshivayu deystviye
#dobavleniye
if info_contact == "добавить":
    name = str(input("Введите имя абонента"))
    if name in names:
        print(input("Такое имя уже существует. Попробуйте другое имя:"))
    else:
        number = input ("Введите номер абонента")
        names.append(name)
        numbers.append(number)
        print(f"Контакт {name} добавлен")
#izmenyayem
elif info_contact == "изменить":
    name = input("Введите имя для изменения:")
    if name in names:
        index = names.index (name)
        new_name = input("Введите новую имю абонента")
        print(f'Абонента {name} изменен на {new_name}')
    else:
        print("Такого абонента не существует")
elif info_contact == "удалить":
    name = input("Введите имя абонента для удаления")
    if name in names:
        index = names.index(name)
        names.pop(index)
        print(f'Абонент {name} удален')
else:
    print(f'Контакт с именем {name} не найден' )