from random import randint
import prompt


def get_progression():
    size = randint(5, 10)
    start = randint(1, 100)
    step = randint(2, 10)
    progression = [start + step * i for i in range(size)]
    return progression


def hide_number(progression):
    index = randint(0, len(progression) - 1)
    result = progression[index]
    progression[index] = "..."
    return result, progression


def game_over(answer, result, name):
    print(f'{answer} is wrong answer ;(.')
    print(f'Correct answer was {result}')
    print(f"Let's try again, {name}!")


def game_progression(name):
    print('What number is missing in the progression?')
    game_round = 0
    while True:
        game_round += 1
        progression = get_progression()
        result, question = hide_number(progression)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if game_round == 3:
            print(f'Congratulations, {name}!')
            break
        elif answer == str(result):
            print('Correct!')
        else:
            game_over(answer, result, name)
            break
