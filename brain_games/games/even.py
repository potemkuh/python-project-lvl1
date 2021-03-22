import prompt
from random import randint

STAR_NUMBERS = 0
END_NUMBERS = 99


def question_and_answer():
    question = randint(STAR_NUMBERS, END_NUMBERS)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
