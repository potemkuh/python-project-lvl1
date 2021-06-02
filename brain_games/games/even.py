from random import randint

START_NUMBERS = 0
END_NUMBERS = 99


def question_and_answer():
    question = randint(START_NUMBERS, END_NUMBERS)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
