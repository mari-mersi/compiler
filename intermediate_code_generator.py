# Пример функции для генерации промежуточного кода из AST
from semantic import *

def generate_intermediate_code(parsed_tree):
    intermediate_code = []

    for statement in parsed_tree:
        if statement[0] == 'assign':
            variable_name, expression = statement[1], statement[2]
            code = generate_expression_code(expression)
            intermediate_code.append(f'{variable_name} = {code};')

    return intermediate_code

def generate_expression_code(expression):
    if isinstance(expression, tuple):
        operator = expression[0]
        if operator == 'assign':
            variable_name, value_expression = expression[1], expression[2]
            value_code = generate_expression_code(value_expression)
            return f'{variable_name} = {value_code}'
        elif operator in ('+', '-', '*', '/'):
            left_expression, right_expression = expression[1], expression[2]
            left_code = generate_expression_code(left_expression)
            right_code = generate_expression_code(right_expression)
            return f'({left_code} {operator} {right_code})'
        elif operator == 'number':
            return str(expression[1])
        elif operator == 'id':
            return expression[1]
    elif isinstance(expression, str):
        return expression
    else:
        return str(expression)

# Пример использования
print("intermediate_code_generator")
input_program = "x := 10.5; y := (x * 2) + 3.14"
parsed_tree = parser.parse(input_program)

intermediate_code = generate_intermediate_code(parsed_tree)
for line in intermediate_code:
    print(line)
