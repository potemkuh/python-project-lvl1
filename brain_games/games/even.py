import prompt
import random


def answer(num, answer):
    if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
        return True
    else:
        return False


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


def parity_number(name):
    round = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while round != 3:
        number = random.randint(0, 10)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if answer(number, user_answer) == True:
            round += 1
            print('Correct!')
        else:
            return game_over(user_answer, name)
    print(f'Congratulations, {name}!')


name = 'gg'
parity_number(name)