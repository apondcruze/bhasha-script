import ply.lex as lex
import ply.yacc as yacc

# --- 1. LEXER SECTION ---
def bangla_to_eng(bn_str):
    bn_digits = "০১২৩৪৫৬৭৮৯"
    eng_digits = "0123456789"
    mapping = str.maketrans(bn_digits, eng_digits)
    return bn_str.translate(mapping)

# Updated keywords: TAHOLE and NAHOLE
tokens = ('DHORO', 'DEKHAO', 'JODI', 'TAHOLE', 'NAHOLE', 'ID', 'NUMBER', 'EQUALS', 'GT', 'LT')
literals = ['+', '-', '*', '/', '(', ')']

t_EQUALS = r'='
t_GT     = r'>'
t_LT     = r'<'
t_ignore = ' \t'

def t_JODI(t): r'jodi'; return t
def t_TAHOLE(t): r'tahole'; return t
def t_NAHOLE(t): r'nahole'; return t
def t_DHORO(t): r'dhoro'; return t
def t_DEKHAO(t): r'dekhao'; return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'[0-9০-৯]+'
    t.value = int(bangla_to_eng(t.value))
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# General Error message
def t_error(t):
    raise Exception(f"Bhul hoyeche! '{t.value[0]}' ti ekhane thik noy.")

lexer = lex.lex()

# --- 2. PARSER SECTION ---
variables = {}
last_output = ""

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
)

def p_statement_assign(p):
    'statement : DHORO ID EQUALS expression'
    variables[p[2]] = p[4]

def p_statement_print(p):
    'statement : DEKHAO expression'
    global last_output
    last_output = str(p[2])

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

# Updated with TAHOLE and NAHOLE rules
def p_statement_if_else(p):
    '''statement : JODI expression GT expression TAHOLE statement NAHOLE statement
                 | JODI expression LT expression TAHOLE statement NAHOLE statement'''
    condition = False
    if p[3] == '>': condition = p[2] > p[4]
    elif p[3] == '<': condition = p[2] < p[4]
    
    p[0] = p[6] if condition else p[8]

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_group(p):
    "expression : '(' expression ')' "
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = variables.get(p[1], 0)

# Syntax Error message
def p_error(p):
    if p:
        raise Exception(f"Syntax bhul hoyeche! '{p.value}' er kache kothao bhul ache.")
    else:
        raise Exception("Syntax bhul hoyeche! Code kothao baki ache.")

parser = yacc.yacc()