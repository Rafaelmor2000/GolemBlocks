import ply.yacc as yacc
import sys
import GolemLex

tokens = GolemLex.tokens
allGood = True

def error():
    global allGood
    allGood = False



def p_programa(p):
    'programa : PROGRAM ID LBRACE programaDec programaFunc MAIN LPAREN RPAREN LBRACE programaDec bloque RBRACE RBRACE'

def p_programaDec(p):
    '''programaDec : declaracion programaDec
        | empty'''
    
def p_programaFunc(p):
    '''programaFunc : function programaFunc
        | empty'''

def p_declaracion(p):
    'declaracion : VAR tipo ID decArr SEMICOLON'

def p_decArr(p):
    '''decArr : LBRACKET CTE_I RBRACKET decMat
        | empty'''

def p_decMat(p):
    '''decMat : LBRACKET CTE_I RBRACKET
        | empty'''


def p_function(p):
    'function : FUNCTION funcType ID LPAREN param RPAREN LBRACE programaDec bloque return RBRACE'

def p_funcType(p):
    '''funcType : tipo
        | VOID'''

def p_param(p):
    '''param : tipo ID params
        | empty'''
    
def p_params(p):
    '''params : COMMA tipo ID params
        | empty'''
    
def p_tipo(p):
    '''tipo : INT
        | FLOAT
        | BOOL
        | CHAR
        | STRING'''

def p_bloque(p):
    '''bloque : asignacion bloque
        | condicion bloque
        | escritura bloque
        | ciclos bloque
        | lectura bloque
        | llamada SEMICOLON bloque
        | empty'''

def p_return(p):
    '''return : RETURN expression SEMICOLON
        | empty'''

def p_asignacion(p):
    'asignacion : ID asigArr EQUAL expression SEMICOLON'

def p_asigArr(p):
    '''asigArr : LBRACKET expression RBRACKET asigMat
        | empty'''
    
def p_asigMat(p):
    '''asigMat : LBRACKET expression RBRACKET
        | empty'''

def p_condicion(p):
    'condicion : IF LPAREN expression RPAREN LBRACE bloque RBRACE else'

def p_else(p):
    '''else : ELSE LBRACE bloque RBRACE
        | ELSE condicion
        | empty'''

def p_escritura(p):
    'escritura : PRINT LPAREN texto RPAREN SEMICOLON'

def p_texto(p):
    '''texto : expression textos
        | CTE_S textos'''

def p_textos(p):
    '''textos : COMMA texto
        | empty'''

def p_ciclos(p):
    '''ciclos : while
        | doWhile'''

def p_while(p):
    'while : WHILE LPAREN expression RPAREN LBRACE bloque RBRACE'

def p_doWhile(p):
    'doWhile : DO LBRACE bloque RBRACE WHILE LPAREN expression RPAREN SEMICOLON'

def p_lectura(p):
    'lectura : INPUT LPAREN variable lecturas RPAREN SEMICOLON'

def p_lecturas(p):
    '''lecturas : COMMA variable lecturas
        | empty'''

def p_llamada(p):
    '''llamada : ID LPAREN llama RPAREN
        | POW LPAREN llama RPAREN
        | SQRT LPAREN llama RPAREN
        | CBRT LPAREN llama RPAREN'''

def p_llama(p):
    '''llama : expression llamas
        | empty'''

def p_llamas(p):
    '''llamas : COMMA expression llamas
        | empty'''

def p_expression(p):
    '''expression : NOT LPAREN expression RPAREN
        | LPAREN expression gate expression RPAREN
        | boolExp'''

def p_gate(p):
    '''gate : AND
        | OR
        | XOR'''

def p_boolExp(p):
    '''boolExp : arithmetic
        | arithmetic LTHAN arithmetic
        | arithmetic GTHAN arithmetic
        | arithmetic LEQUAL arithmetic
        | arithmetic GEQUAL arithmetic
        | arithmetic DIFFERENCE arithmetic
        | arithmetic EQUALS arithmetic'''

def p_arithmetic(p):
    '''arithmetic : termino
        | termino PLUS termino
        | termino MINUS termino'''

def p_termino(p):
    '''termino : factor
        | factor TIMES factor
        | factor DIVIDE factor
        | factor MOD factor'''

def p_factor(p):
    '''factor : LPAREN expression RPAREN
        | var_cte
        | llamada
        | variable'''

def p_var_cte(p):
    '''var_cte : CTE_C
        | CTE_S
        | CTE_I
        | CTE_F
        | TRUE
        | FALSE'''

def p_variable(p):
    '''variable : ID asigArr'''

def p_empty(p):
    'empty : '

def p_error(p):
    error()
    print(f'Syntax error at {p.value!r}')
    


# Build the parser
parser = yacc.yacc()

#temporary input
if __name__ == '__main__':
    fileName = sys.argv[1]
    
    inputFile = open(fileName, 'r')
    inputCode = inputFile.read()
    inputFile.close()

    parser.parse(inputCode)
    if allGood:
        print("All good!")