import ply.yacc as yacc
from lexer import tokens  # Импортируем токены из лексического анализатора (lexer.py)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'),
)

def p_statements(p):
    '''statements : statements SEMICOLON statement
                  | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_statement_assign(p):
    'statement : ID ASSIGN expression'
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_expression_parentheses(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Синтаксическая ошибка")

# Правила для операторов
def p_expression_uminus(p):
    '''expression : MINUS expression %prec UMINUS'''
    p[0] = ('UMINUS', p[2])

parser = yacc.yacc()


