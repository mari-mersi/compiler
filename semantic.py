import ply.yacc as yacc
import ply.lex as lex
from lexer import tokens
from parser import *

# Глобальный словарь для хранения переменных
variables = {}

# Функция для выполнения операции присваивания
def assign_variable(name, value):
    variables[name] = value

# Функция для вычисления арифметических выражений
def evaluate_expression(expression):
    if isinstance(expression, (int, float)):
        return expression
    elif isinstance(expression, tuple):
        op = expression[0]
        if op == 'UMINUS':
            return -evaluate_expression(expression[1])
        elif op == 'number':
            return expression[1]
        elif op == 'id':
            if expression[1] in variables:
                return variables[expression[1]]
            else:
                raise Exception(f"Ошибка: Идентификатор '{expression[1]}' не определен.")
        elif op in ('+', '-', '*', '/'):
            left = evaluate_expression(expression[1])
            right = evaluate_expression(expression[2])
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    raise Exception("Ошибка: Деление на ноль.")
                return left / right
        else:
            raise Exception(f"Ошибка: Неизвестный оператор '{op}'.")

# Функция для выполнения семантического анализа
def semantic_analysis(tree):
    for node in tree:
        if node[0] == 'assign':
            name = node[1]
            value = evaluate_expression(node[2])
            assign_variable(name, value)

print("semantic")
'''input_program = "x := 10.5; y := (x * 2) + 3.14"
parsed_tree = parser.parse(input_program)
semantic_analysis(parsed_tree)
print(variables)  # Вывести значения переменных после семантического анализа
print()'''