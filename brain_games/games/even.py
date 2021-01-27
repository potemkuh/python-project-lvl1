import prompt
import random


def parity_number(name):
    round_counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while round_counter < 3:
        round_counter += 1
        question = random.randint(0, 10)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if round_counter == 3:
            print(f"Congratulations, {name}")
        elif question % 2 == 0 and answer == 'yes' or
        question % 2 != 0 and answer == 'no':
            print('Correct!')
        elif question % 2 != 0 and answer == 'yes' or
        question % 2 == 0 and answer == 'no':
            if question % 2 != 0 and answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
            break
        else:
            print(f"{answer} is wrong answer ;(.")
            print(f"Let's try again, {name}!")
