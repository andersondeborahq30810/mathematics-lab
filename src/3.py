import math

def solve_mathematics_problem(problem):
    """
    Solve a mathematics problem using Python.
    :param problem: A string representing the problem to be solved.
    :return: The solution to the problem.
    """
    # Split the problem into individual parts
    parts = problem.split(" ")

    # Extract the operation and operands from the parts
    operation = parts[1]
    operand1 = int(parts[2])
    operand2 = int(parts[4])

    # Perform the operation
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    elif operation == "*":
        result = operand1 * operand2
    else:
        raise ValueError("Unsupported operation")

    # Return the solution
    return result

# Test the function with a sample problem
problem = "What is 3 + 5?"
solution = solve_mathematics_problem(problem)
print(f"Solution to {problem} is {solution}")