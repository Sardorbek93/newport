class Animal:
    def __init__(self, skin):
        self. skin = skin

    def make_sound(self, sound):
        print(sound)

class Horse(Animal):
    def __init__(self, skin, fur):
        super().__init__(skin)
        self.fur = fur

    def skachka(self):
        print('loshad skachet')
class Cat (Animal):
    def murchat(self):
        print("Кошка мурчит")

class FISH (Animal):
    pass   # ЧтобЫ не распостраняло наследование Animal!!!


barni = Horse(skin = 'black', fur = 'oxoxoxo')
KoshkaTom = Cat ('MYAU')
Sushestvo = Animal('all')
barni.make_sound("igogo")
barni.skachka()
KoshkaTom.make_sound("myau")
KoshkaTom.murchat()
Sushestvo.make_sound('sadsfdsdsv')