from argparse import Action


def action ():
#     if int (a) % 2 == 0:
#         print(f' Число {a} четное')
#     elif int (a) % 2 == 1:
#         print(f'число {a} нечотное')
# while True:
#


    while True:
        num = int(input("Введите число"))
        if num % 2 == 0:
            print('chotnoe')
        elif num % 2 == 1:
            print('nechotnoe')
action()
