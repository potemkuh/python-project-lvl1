import random
import prompt


def question_and_answer():
    #size = random.randint(5, 10)
    start = random.randint(1, 100)
    step = random.randint(2, 10)
    question = [start + step * i for i in range(10)]
    index = random.randint(0, len(question) - 1)
    result = question[index]
    question[index] = "..."
    new = ' '.join(question)
    return str(new), result
