import random
import prompt


def calculator(name):
    round_counter = 0
    print('What is the result of the expression?')
    while True:
        round_counter += 1
        num1 = andom.randint(1, 20)
        num2 = andom.randint(1, 10)
        action = random.choice(['+', '-', '*'])
        if round_counter == 4:
            print(f'Congratulations, {name}!')
            break
        elif action == "+":
            print(f'Question: {num1} {action} {num2}')
            answer = prompt.string('Your answer: ')
            if int(answer) == num1 + num2:
                print('Correct!')
            else:
                print(f'{answer} is wrong answer ;(.')
                print(f'Correct answer was {num1 + num2}')
                print(f"Let's try again, {name}!"))
                break
        elif action == "-":
            print(f'Question: {num1} {action} {num2}')
            answer = prompt.string('Your answer: ')
            if int(answer) == num1 - num2:
                print('Correct!')
            else:
                print(f'{answer} is wrong answer ;(.')
                print(f'Correct answer was {num1 - num2}')
                print(f"Let's try again, {name}!")
                break
        elif action == "*":
            print(f'Question: {num1} {action} {num2}')
            answer = prompt.string('Your answer: ')
            if int(answer) == num1 * num2:
                print('Correct!')
            else:
                print(f'{answer} is wrong answer ;(.')
                print(f'Correct answer was {num1 * num2}')
                print(f"Let's try again, {name}!")
                break
