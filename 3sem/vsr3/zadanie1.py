from random import *


def main():
    guess = randint(0, 100)
    x = None
    more = 'Число больше'
    less = 'Число меньше '
    print('Угадайте какое будет число: ')
    while x != guess:
        x = int(input())
        if x < guess:
            print('Не угадали, {}'.format(more))
        elif x > guess:
            print('Не угадали, {}'.format(less))
        else:
            print('Угадали!')


main()
