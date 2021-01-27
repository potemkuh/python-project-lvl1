import random
import prompt


def math_action():
    return random.choice(['+', '-', '*'])


def rand_number():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 20)
    return number1, number2


def calculator(name):
    round_counter = 0
    print('What is the result of the expression?')
    while True:
        round_counter += 1
        num1, num2 = rand_number()
        action = math_action()
        if round_counter == 4:
            print(f'Congratulations, {name}!')
            break
        elif action == "+":
            print(f'Question: {num1} {action} {num2}')
            answer = prompt.string('Your answer: ')
            if int(answer) == num1 + num2:
                print('Correct!')
            else:
                print(
                    f'{answer} is wrong answer ;(. Correct answer was {num1 + num2}'
                )
                print(f"Let's try again, {name}!")
                break
        elif action == "-":
            print(f'Question: {num1} {action} {num2}')
            answer = prompt.string('Your answer: ')
            if int(answer) == num1 - num2:
                print('Correct!')
            else:
                print(
                    f'{answer} is wrong answer ;(. Correct answer was {num1 - num2}'
                )
                print(f"Let's try again, {name}!")
                break
        elif action == "*":
            print(f'Question: {num1} {action} {num2}')
            answer = prompt.string('Your answer: ')
            if int(answer) == num1 * num2:
                print('Correct!')
            else:
                print(
                    f'{answer} is wrong answer ;(. Correct answer was {num1 * num2}'
                )
                print(f"Let's try again, {name}!")
                break
