import ply.lex as lex
import ply.yacc as yacc
from typing import List, Any

tokens = [
    'IDENTIFIER',
    'STRING',
    'NUMBER',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'GREATER',
    'LESS',
    'GREATEREQUAL',
    'LESSEQUAL',
    'NOTEQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'TRAEME',
    'TODO',
    'DE_LA_TABLA',
    'DONDE',
    'AGRUPANDO_POR',
    'MEZCLANDO',
    'EN',
    'LOS_DISTINTOS',
    'CONTANDO',
    'METE_EN',
    'LOS_VALORES',
    'ACTUALIZA',
    'SETEA',
    'BORRA_DE_LA',
    'ORDENA_POR',
    'COMO_MUCHO',
    'WHERE_DEL_GROUP_BY',
    'EXISTE',
    'EN_ESTO',
    'ENTRE',
    'PARECIDO_A',
    'ES_NULO',
    'CAMBIA_LA_TABLA',
    'AGREGA_LA_COLUMNA',
    'ELIMINA_LA_COLUMNA',
    'CREA_LA_TABLA',
    'TIRA_LA_TABLA',
    'POR_DEFECTO',
    'UNICO',
    'CLAVE_PRIMA',
    'CLAVE_REFERENTE',
    'NO_NULO',
    'TRANSFORMA_A',
    'AND',
    'OR',
]

# Regular expressions for simple tokens
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_NOTEQUAL = r'<>|!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Regular expressions for USQL tokens
t_TRAEME = r'TRAEME'
t_TODO = r'TODO'
t_DE_LA_TABLA = r'DE LA TABLA'
t_DONDE = r'DONDE'
t_AGRUPANDO_POR = r'AGRUPANDO POR'
t_MEZCLANDO = r'MEZCLANDO'
t_EN = r'EN'
t_LOS_DISTINTOS = r'LOS DISTINTOS'
t_CONTANDO = r'CONTANDO'
t_METE_EN = r'METE EN'
t_LOS_VALORES = r'LOS VALORES'
t_ACTUALIZA = r'ACTUALIZA'
t_SETEA = r'SETEA'
t_BORRA_DE_LA = r'BORRA DE LA'
t_ORDENA_POR = r'ORDENA POR'
t_COMO_MUCHO = r'COMO MUCHO'
t_WHERE_DEL_GROUP_BY = r'WHERE DEL GROUP BY'
t_EXISTE = r'EXISTE'
t_EN_ESTO = r'EN ESTO:'
t_ENTRE = r'ENTRE'
t_PARECIDO_A = r'PARECIDO A'
t_ES_NULO = r'ES NULO'
t_CAMBIA_LA_TABLA = r'CAMBIA LA TABLA'
t_AGREGA_LA_COLUMNA = r'AGREGA LA COLUMNA'
t_ELIMINA_LA_COLUMNA = r'ELIMINA LA COLUMNA'
t_CREA_LA_TABLA = r'CREA LA TABLA'
t_TIRA_LA_TABLA = r'TIRA LA TABLA'
t_POR_DEFECTO = r'POR DEFECTO'
t_UNICO = r'UNICO'
t_CLAVE_PRIMA = r'CLAVE PRIMA'
t_CLAVE_REFERENTE = r'CLAVE REFERENTE'
t_NO_NULO = r'NO NULO'
t_TRANSFORMA_A = r'TRANSFORMA A'

# Tokens for logical operators
t_AND = r'AND'
t_OR = r'OR'

# Ignored characters
t_ignore = ' \t'



USQL_TO_SQL = {
    'TRAEME': 'SELECT',
    'TODO': '*',
    'DE LA TABLA': 'FROM',
    'DONDE': 'WHERE',
    'AGRUPANDO POR': 'GROUP BY',
    'MEZCLANDO': 'JOIN',
    'EN': 'ON',
    'LOS DISTINTOS': 'DISTINCT',
    'CONTANDO': 'COUNT',
    'METE EN': 'INSERT INTO',
    'LOS VALORES': 'VALUES',
    'ACTUALIZA': 'UPDATE',
    'SETEA': 'SET',
    'BORRA DE LA': 'DELETE FROM',
    'ORDENA POR': 'ORDER BY',
    'COMO MUCHO': 'LIMIT',
    'WHERE DEL GROUP BY': 'HAVING',
    'EXISTE': 'EXISTS',
    'EN ESTO:': 'IN',
    'ENTRE': 'BETWEEN',
    'PARECIDO A': 'LIKE',
    'ES NULO': 'IS NULL',
    'CAMBIA LA TABLA': 'ALTER TABLE',
    'AGREGA LA COLUMNA': 'ADD COLUMN',
    'ELIMINA LA COLUMNA': 'DROP COLUMN',
    'CREA LA TABLA': 'CREATE TABLE',
    'TIRA LA TABLA': 'DROP TABLE',
    'POR DEFECTO': 'DEFAULT',
    'UNICO': 'UNIQUE',
    'CLAVE PRIMA': 'PRIMARY KEY',
    'CLAVE REFERENTE': 'FOREIGN KEY',
    'NO NULO': 'NOT NULL',
    'TRANSFORMA A': 'CAST',
}

SQL_TO_USQL = {v: k for k, v in USQL_TO_SQL.items()}

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_STRING(t):
    r'\'(.*?)\''
    return t

def t_NUMBER(t):
    r'\d+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser rules
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement(p):
    '''statement : select_statement SEMICOLON
                 | insert_statement SEMICOLON
                 | update_statement SEMICOLON
                 | delete_statement SEMICOLON
                 | alter_table_statement SEMICOLON'''
    pass

def p_select_statement(p):
    '''select_statement : TRAEME select_items DE_LA_TABLA table_name optional_where'''
    pass

def p_select_items(p):
    '''select_items : TODO
                    | LOS_DISTINTOS IDENTIFIER
                    | IDENTIFIER'''
    pass

def p_table_name(p):
    '''table_name : IDENTIFIER'''
    pass

def p_optional_where(p):
    '''optional_where : DONDE conditions
                      | empty'''
    pass

def p_conditions(p):
    '''conditions : condition
                  | conditions logical_operator condition'''
    pass

def p_condition(p):
    '''condition : IDENTIFIER comparison_operator value'''
    pass

def p_comparison_operator(p):
    '''comparison_operator : EQUALS
                           | GREATER
                           | LESS
                           | GREATEREQUAL
                           | LESSEQUAL
                           | NOTEQUAL'''
    pass

def p_value(p):
    '''value : STRING
             | NUMBER
             | IDENTIFIER'''
    pass

def p_logical_operator(p):
    '''logical_operator : AND
                        | OR'''
    pass

def p_insert_statement(p):
    '''insert_statement : METE_EN table_name LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPAREN'''
    pass

def p_update_statement(p):
    '''update_statement : ACTUALIZA table_name SETEA assignment_list optional_where'''
    pass

def p_delete_statement(p):
    '''delete_statement : BORRA_DE_LA table_name optional_where'''
    pass

def p_alter_table_statement(p):
    '''alter_table_statement : CAMBIA_LA_TABLA table_name alter_action'''
    pass

def p_column_list(p):
    '''column_list : column_list COMMA IDENTIFIER
                   | IDENTIFIER'''
    pass

def p_value_list(p):
    '''value_list : value_list COMMA value
                  | value'''
    pass

def p_assignment_list(p):
    '''assignment_list : assignment_list COMMA assignment
                       | assignment'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS value'''
    pass

def p_alter_action(p):
    '''alter_action : AGREGA_LA_COLUMNA IDENTIFIER data_type constraints
                    | ELIMINA_LA_COLUMNA IDENTIFIER'''
    pass

def p_data_type(p):
    '''data_type : IDENTIFIER LPAREN NUMBER RPAREN
                 | IDENTIFIER'''
    pass

def p_constraints(p):
    '''constraints : constraints constraint
                   | constraint
                   | empty'''
    pass

def p_constraint(p):
    '''constraint : NO_NULO
                  | POR_DEFECTO value
                  | UNICO
                  | CLAVE_PRIMA
                  | CLAVE_REFERENTE'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token {p.type} (valor: {p.value}) en la linea {p.lineno}")
        raise SyntaxError(f"Error de sintaxis {p.type}")
    else:
        print("Error de sintaxis")
        raise SyntaxError("Error de sintaxis EOF") 

parser = yacc.yacc()