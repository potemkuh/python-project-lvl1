from math import sqrt
from random import randint
import prompt

STAR_NUMBERS = 1
END_NUMBERS = 99


def is_prime():
    if num < 2:
        return False
    if num == 2:
        return True
    limit = sqrt(num)
    i = 2
    while i <= limit:
        if num % i == 0:
            return False
        i += 1
    return True


def question_and_answer():
    question = randint(STAR_NUMBERS, END_NUMBERS)
    result = 'yes' if is_prime(question) else 'no'
    return question, result
