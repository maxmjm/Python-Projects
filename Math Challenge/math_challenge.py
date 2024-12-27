import random 

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 4
MAX_OPERAND = 14
TOTAL_PROBLEMS = 10

def generate_problem():
    left_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left_operand) + " " + operator + " " + str(right_operand)

    answer = eval(expression)

    return expression, answer

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True: 
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ") 
        if guess == str(answer):
            break
        