import random
import prompt


def get_progression():
    size = random.randint(5, 10)
    start = random.randint(1, 100)
    step = random.randint(2, 10)
    progression = [start + step * i for i in range(size)]
    return progression


def hide_number(progression):
    index = random.randint(0, len(progression) - 1)
    result = progression[index]
    progression[index] = ".."
    return result, progression


def game_over(answer, result, name):
    print(f'{answer} is wrong answer ;(.')
    print(f'Correct answer was {result}')
    print(f"Let's try again, {name}!")


def game_progression(name):
    print('What number is missing in the progression?')
    game_round = 0
    while game_round < 3:
        progression = get_progression()
        result, question = hide_number(progression)
        print('Question:', ' '.join(map(str, question)))
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            game_round += 1
            print('Correct!')
        else:
            return game_over(answer, result, name)
    print(f'Congratulations, {name}!')
