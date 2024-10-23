class Animal:
    def make_sound(self, sound):
        print(sound)

class Horse(Animal):
    def skachka (self):
        print("лошадь скачет")

class Cat (Animal):
    def murchat(self):
        print("Кошка мурчит")

class FISH (Animal):
    pass   # ЧтобЫ не распостраняло наследование Animal!!!

barni = Horse()
KoshkaTom = Cat ()
Sushestvo = Animal()
barni.make_sound("igogo")
barni.skachka()
KoshkaTom.make_sound("myau")
KoshkaTom.murchat()
Sushestvo.make_sound('sadsfdsdsv')