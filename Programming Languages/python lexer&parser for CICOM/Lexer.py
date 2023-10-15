import ply.lex as lex
from ply.lex import TOKEN

reserved = {
        "map" :"MAP",
        "if": "IF",
        "else": "ELSE",
        "then": "THEN",
        "to": "TO",
        "in": "IN",
        "let": "LET",
        "true": "TRUE",
        "false": "FALSE",
        "number?": "NUMQ",
        "function?": "FUNCTQ",
        "list?": "LISTQ",
        "empty?": "EMPTYQ",
        "cons?": "CONSQ",
        "cons": "CONS",
        "first": "FIRST",
        "rest": "REST",
        "arity": "ARITY"
}

tokens =  [
    'SPAR',
    'EPAR',
    'COMA',
    'ASSIGN',
    'SEMI',
    'APROX',
    'MINUS',
    'SYMBOL',
    'INT',
    'PLUS',
    'ID',
    'NEWLINE',
]

tokens += reserved.values()

digit         = '[0-9]'
char          = '[a-z]|[A-Z]|\?|_'
delim         = r'\(|\)|\[|\]|,|;'
operations    = r'\+|\-|~|\*|\/|=|!=|>|<|>=|<=|&|\||:='
identificator = fr'({char})(({char})|({digit}))*'

t_MAP     = r'map' 
t_INT     = fr'({digit})+'
t_SPAR    = r'\('
t_EPAR    = r'\)'
t_COMA    = r','
t_ASSIGN  = r':='
t_SEMI    = r';'
t_APROX   = r'~'
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_SYMBOL  = r'\*|\/|=|!=|>=|<=|<|>|&|\|'
t_ignore = r' '

def t_NEWLINE(t):
    r'\n'
    t.type = t_ignore

@TOKEN(identificator)
def t_ID(t):
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_error(t):
    print(f'Illegal Character: {t.value}')
    t.lexer.skip(1)
lex.lex()


#FOR TESTING WITHOUT TESTING PARSER
# if __name__ == '__main__':
#     with open('tests/test','r') as c:
#         lex.input(c.read())
#         while True:
#             tok = lex.token()
#             if not tok:
#             # stops at EOL
#                 break
#             print(f'[{tok.type}] found: [{tok.value}]')