from random import randint
from math import gcd
import prompt

STAR_NUMBERS = 1
END_NUMBERS = 99


def question_and_answer():
    num1 = randint(STAR_NUMBERS, END_NUMBERS)
    num2 = randint(STAR_NUMBERS, END_NUMBERS)
    question = f'{num1} {num2}'
    result = gcd(num1, num2)
    return question, result
