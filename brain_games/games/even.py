import prompt
import random


def answer(num, answer):
    if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
        return True
    else:
        return False


def parity_number(name):
    game_round = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while game_round < 3:
        game_round += 1
        number = random.randint(0, 10)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if game_round == 3:
            print(f"Congratulations, {name}")
            break
        else:
            if answer(number, user_answer) is True:
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. ")
                print(f"Let's try again, {name}!")
                break
