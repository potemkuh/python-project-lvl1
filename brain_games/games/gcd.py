from random import randint
from math import gcd
import prompt


def game_over():
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{gcd(number_a,number_b)}'."
    )
    print(f"Let's try again, {name}!")


def game_nod(name):
    print('Find the greatest common divisor of given numbers.')
    game_round = 0
    while True:
        number_a = randint(1, 100)
        number_b = randint(1, 100)
        game_round += 1
        print(f'Question: {number_a} {number_b}')
        answer = prompt.string('Your answer: ')
        if game_round == 3:
            print(f'Congratulations, {name}!')
            return
        elif answer == str(gcd(number_a, number_b)):
            print('Correct!')
        else:
            game_over()
            return


name = 'gg'
game_nod(name)