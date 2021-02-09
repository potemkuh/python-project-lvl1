from math import sqrt
from random import randint
import prompt


def game_over(answer, name):
    if answer == 'yes':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
        print(f"Let's try again, {name}!")
    elif answer == 'no':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
        print(f"Let's try again, {name}!")
    else:
        print(f"'{answer}' is wrong answer ;(.")
        print(f"Let's try again, {name}!")


def is_prime(num):
    if num < 2:
        return 'no'
    if num == 2:
        return 'yes'
    limit = sqrt(num)
    i = 2
    while i <= limit:
        if num % i == 0:
            return 'no'
        i += 1
    return 'yes'


def game_prime(name):
    game_round = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while game_round < 3:
        number = randint(2, 500)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if is_prime(number) == user_answer:
            game_round += 1
            print('Correct!')
        else:
            return game_over(user_answer, name)
    print(f'Congratulations, {name}!')
