import random


def is_valid(a):
    return a.isdigit() and 0 < int(a) < int(num1)

def game():
    counter = 0
    while True:
        b = input(f'Введите число от 1 до {num1}: ')
        if not is_valid(b):
            print(f'А может быть все-таки введем целое число от 1 до {num1} ?')
            continue
        b = int(b)
        counter += 1
        if b < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            print('Число попыток: ', counter)
        elif b > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            print('Число попыток: ', counter)
        else:
            print('Вы угадали, поздравляем!')
            print('Число попыток: ', counter)
            break





print('Добро пожаловать в числовую угадайку')

while True:
    num1 = input('Создадим случайное число от 1 до .. Введите это число ')
    num = random.randint(1, int(num1))
    game()
    if 'да' != input('Сыграем еще? (да/нет) ? '):
        print('Игра окончена. Удачи с числами.')
        break

