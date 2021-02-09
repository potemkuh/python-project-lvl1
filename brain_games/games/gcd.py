from random import randint
from math import gcd
import prompt


def game_over(answer, name, result):
    print(f"'{answer}' is wrong answer ;(.")
    print(f"Correct answer was '{result}'.")
    print(f"Let's try again, {name}!")


def get_numbers():
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    return number_a, number_b


def answer(arg_1, arg_2):
    if arg_1 == arg_2:
        return True
    return False


def game_nod(name):
    print('Find the greatest common divisor of given numbers.')
    game_round = 0
    while game_round < 3:
        num_1, num_2 = get_numbers()
        result = gcd(num_1, num_2)
        print(result)
        print(f'Question: {num_1} {num_2}')
        user_answer = prompt.string('Your answer: ')
        if answer(int(user_answer), result) == True:
            game_round += 1
            print('Correct!')
        else:
            return game_over(user_answer, name, result)
    print(f'Congratulations, {name}!')