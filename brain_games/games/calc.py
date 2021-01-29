from random import randint, choice
import prompt


def get_numbers():
    num_1 = randint(1, 20)
    num_2 = randint(1, 10)
    return num_1, num_2


def get_operator():
    operator = choice(['+', '-', '*'])
    return operator


def game_over(answer, result, name):
    print(f'{answer} is wrong answer ;(.')
    print(f'Correct answer was {result}')
    print(f"Let's try again, {name}!")


def calculator(name):
    game_round = 0
    print('What is the result of the expression?')
    while True:
        game_round += 1
        num_1, num_2 = get_numbers()
        operator = get_operator()
        if game_round == 4:
            print(f'Congratulations, {name}!')
            break
        elif operator == "+":
            print(f'Question: {num_1} {operator} {num_2}')
            answer = prompt.string('Your answer: ')
            if answer == str(num_1 + num_2):
                print('Correct!')
            else:
                result = num_1 + num_2
                game_over(answer, result, name)
                break
        elif operator == "-":
            print(f'Question: {num_1} {operator} {num_2}')
            answer = prompt.string('Your answer: ')
            if answer == str(num_1 - num_2):
                print('Correct!')
            else:
                result = num_1 - num_2
                game_over(answer, result, name)
                break
        elif operator == "*":
            print(f'Question: {num_1} {operator} {num_2}')
            answer = prompt.string('Your answer: ')
            if answer == str(num_1 * num_2):
                print('Correct!')
            else:
                result = num_1 * num_2
                game_over(answer, result, name)
                break
