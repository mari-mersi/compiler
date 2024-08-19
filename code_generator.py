from lexer import lexer
from parser import parser
from semantic import semantic_analysis
from intermediate_code_generator import generate_intermediate_code

def generate_target_code(intermediate_code):
    target_code = []  # Здесь будем хранить целевой код
    for instruction in intermediate_code:
        # Разбираем инструкции из промежуточного кода
        if instruction.startswith('assign'):
            parts = instruction.split(' ')
            variable_name = parts[1]
            expression = ' '.join(parts[3:])
            # Генерируем код присваивания в целевом языке (Python)
            assignment_code = f'{variable_name} = {generate_expression_code(expression)}'
            target_code.append(assignment_code)

    return target_code

def save_target_code(target_code, output_file):
    with open(output_file, 'w') as file:
        for line in target_code:
            file.write(line + '\n')
def generate_expression_code(expression):
    # Ваш код генерации кода для арифметического выражения
    # В данном случае, предположим, что expression содержит корректное арифметическое выражение
    # и мы можем просто вернуть его как строку
    return expression