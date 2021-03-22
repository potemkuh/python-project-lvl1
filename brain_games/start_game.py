import prompt
GAME_ROUND = 3


def play(game=None):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    if game is None:
        return
    round = 0

    while round < GAME_ROUND:
        question, result = game.question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f"Let's try again, {name}!")
            return
        round += 1
    print(f'Congratulations, {name}!')
