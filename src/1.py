import math

def get_random_code():
    numbers = list(range(10))
    operators = ["+", "-", "*", "/"]
    expression = ""
    for i in range(3):
        expression += str(numbers.pop(math.floor(len(numbers) * math.random()))) + operators[math.floor(len(operators) * math.random())]
    return eval(expression)