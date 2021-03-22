from random import randint, choice

STAR_NUMBERS = 0
END_NUMBERS = 99


def get_numbers():
    num_1 = randint(STAR_NUMBERS, END_NUMBERS)
    num_2 = randint(STAR_NUMBERS, END_NUMBERS)
    return num_1, num_2


def get_operator():
    operator = choice(['+', '-', '*'])
    return operator


def correct_answer(n1, n2, operation):
    if operation == '+':
        return n1 + n2
    elif operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2


def question_and_answer():
    num1, num2 = get_numbers()
    operator = get_operator()
    question = f'{num1} {operator} {num2}'
    result = correct_answer(num1, num2, operator)
    return question, result
