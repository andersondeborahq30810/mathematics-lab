import random

def get_random_python_code():
    numbers = list(range(10))
    operators = ['+', '-', '*', '/']
    expressions = []

    for i in range(5):
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        operator = random.choice(operators)
        expression = f'{num1} {operator} {num2}'
        expressions.append(expression)

    return '\n'.join(expressions)