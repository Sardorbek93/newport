class BankAccount:  # Исправлено название класса
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

    def deposit(self, amount):  # Исправлено название метода
        self.balance += amount
        print(f"Баланс пополнен. Текущий баланс: {self.balance}$")

    def cash(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Вы сняли со счета {amount}$")
        else:
            print("Недостаточно средств на счету")

    def check_balance(self):  # Изменено название метода, чтобы избежать конфликта
        print(f'Ваш баланс: {self.balance}$')

USER1 = BankAccount("Jordan")  # Исправлено название класса
while True:
    menu = input("Введите действие: \n"
                 "1. Пополнить баланс \n"
                 "2. Снять деньги \n"
                 "3. Посмотреть баланс \n"
                 "4. Выход из аккаунта\n")  # Добавлен перевод строки
    if menu == "1":
        USER1.deposit(int(input("Введите сумму: ")))  # Исправлено форматирование
    elif menu == "2":
        USER1.cash(int(input("Введите сумму для снятия: ")))  # Исправлено форматирование
    elif menu == "3":
        USER1.check_balance()  # Вызов обновленного метода
    elif menu == "4":  # Исправлено на 'elif' и исправлено отступление
        break
    else:
        print("Некорректный ввод, пожалуйста, попробуйте снова.")  # Добавлена обработка ошибок
