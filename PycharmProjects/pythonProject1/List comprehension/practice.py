#Vitaskivaem perviy index s kajdogo elementa
b = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
b2 = [i[0] for i in b ]
print(b2)

#
nums = [i for i in range (1,21)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]
print(chotnie, nechotnie)

#spisok sozdan
usernames = []
while True:
#klient pishet imya
    user = input('Введите имя:')
#proveryayu yest'li eto imya v spiske navisimo kak vvel klient
    if user.lower() in  [name.lower()for name in usernames]:
        print('Такое имя уже есть')
    else:
        usernames.append(user)
        print('Контакт добавлен')
        print(usernames)