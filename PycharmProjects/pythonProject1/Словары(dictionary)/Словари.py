#Словари - это одна из структур данных, которое хранит в себе множество значений в виде пары (ключ - значение)
a = {"test klyuch": "test znachenie"}
print(a)
print(type(a))

#Вытаскиваем значение
a = {1:2, "a":"b"}

print(a[1])#Если ошибка то код дальше не работает
print(a.get (1)) #код работает дальше, в принте выводит [None]
print(a["a"])
print(a.get("a"))

data = {"name": ["Jordan", "Pavel"],
        'age': (12, 21),
        'job': ['porgrammers', 'f']}
print(data['name'][0], data ['job'][-1])

#БИОГРАФИЯ
bio = {'name':'Sardor',
       'age' : 31,
       'profession': 'python programmer',
       'education':{'school': [198]}}
print(bio.values()) #vitaskivaem znacheniye
print(bio.keys()) #vitaskivaem kluchi
print(bio.items()) #vitaskivaem vse po ocheredi
if 'name' in bio: #проверяем name в ключах
    print("Да, есть")
else:
    print('О чем вы!')
bio['gender'] = 'male' #Добавляем словарь гендер к БИО
print(bio)
bio['education']['university'] = 'KIEV NAU' #Добавляем к эдукейшн университет
print(bio)
bio ['education']['school'].append('gimnaziya') #добавление к школе еще одну школу
print(bio)
#bio.clear() #Очистить все
#bio.pop('age') #Очистить ключ AGE
#bio.popitem() #Удаляет последний добавленный

a = dict(name="Sardor", age = 31) #Создаем словарь
print(a)

#ЦИКЛ for в словаре
bio = {'name':'Sardor', 'age' : 31, 'profession': 'python programmer', 'education':{'school': 198}}
for i,c in bio.items():
    print(i,c)