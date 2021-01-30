from math import sqrt
from random import randint
import prompt


def is_prime(n):
    if n < 2:
        return 'no'
    if n == 2:
        return 'yes'
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return 'no'
        i += 1
    return 'yes'


def game_prime(name):
    game_round = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while True:
        game_round += 1
        number = randint(2, 1000)
        answer = is_prime(number)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if game_round == 3:
            print(f'Congratulations, {name}!')
            return
        elif user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{is_prime(number)}'.")
            print(f"Let's try again, {name}!")
            return
