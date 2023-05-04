import ply.lex as lex

reserved = {
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'function' : 'FUNCTION',
    'var' : 'VAR',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'and' : 'AND',
    'or' : 'OR',
    'xor' : 'XOR',
    'not' : 'NOT',
    'int' : 'INT',
    'float': 'FLOAT',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'string' : 'STRING',
    'void' : 'VOID',
    'while': 'WHILE',
    'do' : 'DO',
    'input' : 'INPUT',
    'return' : 'RETURN',
    'true' : 'TRUE',
    'false' : 'FALSE'
}

# --- Tokenizer
tokens = [ 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'LPAREN', 'RPAREN',
           'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'ID',
           'CTE_I', 'CTE_F', 'CTE_C', 'CTE_S', 'GTHAN', 'LTHAN',
           'GEQUAL', 'LEQUAL', 'EQUAL', 'EQUALS', 'DIFFERENCE', 'SEMICOLON', 'COMMA'] + list(reserved.values())

# Ignored characters
t_ignore = " \t\n"

# Token matching rules are written as regexs
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'

t_GTHAN = r'\>'
t_LTHAN = r'\<'
t_GEQUAL = r'\>='
t_LEQUAL = r'\<='
t_EQUAL = r'='
t_EQUALS = r"=="
t_DIFFERENCE = r"<>"


t_SEMICOLON = r';'
t_COMMA = r','

t_CTE_S= r'"(.*?)"'
t_CTE_C = r'(L)?\'([^\\\n]|(\\.))*?\''

def t_ID(t):
    r'([a-z][a-zA-Z0-9]*)'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_CTE_F(t):
    r'[-]?[0-9]+([.][0-9]+)'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()