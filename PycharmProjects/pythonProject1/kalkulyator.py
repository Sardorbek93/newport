number1 = int (input("Введите первое число:"))
action = input ("выберите +, -, * или /:")
number2 = int (input("введите второе число:"))
# логика
if action == "+":
    print(number1 + number2)
elif action == "-":
    print(number1 - number2)
elif action == "/":
    print(number1 / number2)
elif action == "*":
    print(number1 * number2)
else:
    print("Не того ты писал олень))")
