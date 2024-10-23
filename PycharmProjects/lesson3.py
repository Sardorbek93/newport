#cars = ["GLS600", "X5M", "zeekr", ("hello", "m5"), "go"]
#print(cars[0:3])
#Создаем базу данных с именами и номерами
names = ["VIP"]
rooms = [10]
#polucheniye info ot menedjera
name = input("Vvedite imya novogo klienta:")
room = int(input("Vvedite nomer dlya zaseleniya:"))
if room in rooms:
    print("Dannaya komnata zanyata!")
else:
    names.append(name)
    rooms.append(room)
    print(f"Klient {name} zaselen v komnatu {room}")
    print(names, rooms)