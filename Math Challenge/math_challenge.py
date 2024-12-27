import random 

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 4
MAX_OPERAND = 14
TOTAL_PROBLEMS = 10

def generate_problem():
    left_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left_operand) + " " + operator + str(right_operand)

    answer = eval(expression)

    return expression, answer
