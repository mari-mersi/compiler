import ply.lex as lex

# Определение токенов
tokens = (
    'ID',
    'NUMBER',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
)

# Определение регулярных выражений для токенов
t_ASSIGN = r':='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d*([Ee][+\-]?\d+)?)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Нераспознанный символ: {t.value[0]}")
    t.lexer.skip(1)

# Создание лексического анализатора
lexer = lex.lex()
print("lexer:")
for token in tokens:
    print(token)
print()