import ply.yacc as yacc
import Lexer
import sys

tokens = Lexer.tokens

def p_Exp(p):
    '''
    Exp : Term
            | Term Binop 
            | Term Binop Exp
            | IF Exp THEN Exp ELSE Exp
            | LET MultiDef IN Exp
            | MAP IdList TO Exp
    '''

def p_Term(p):
    '''
    Term : Unop Term
        | Factor
        | Factor SPAR ExpList EPAR
        | Empty
        | INT
        | Bool
    '''
def p_Factor(p):
    '''
    Factor : SPAR Exp EPAR 
            | Prim
            | ID

    '''
def p_ExpList(p):
    '''
    ExpList : PropExpList
    '''

def p_PropExpList(p):
    '''
    PropExpList : Exp 
                | Exp COMA PropExpList
    '''

def p_IdList(p):
    '''
    IdList : PropIdList
    '''

def p_PropIdList(p):
    '''
    PropIdList : ID
                | ID COMA PropIdList
    '''

def p_Def(p):
    '''
    Def : ID ASSIGN Exp SEMI
    '''

def p_Empty(p):
    '''
    Empty : empty
    '''

def p_Bool(p):
    '''
    Bool : TRUE
        | FALSE
    '''

def p_Unop(p):
    '''
    Unop : Sign 
        | APROX
    '''

def p_Sign(p):
    '''
    Sign : PLUS
        | MINUS
    '''

def p_Binop(p):
    '''
    Binop : Sign
        | SYMBOL
    '''

def p_Prim(p):
    '''
    Prim : NUMQ 
        | FUNCTQ
        | LISTQ
        | EMPTYQ
        | CONSQ
        | CONS
        | FIRST
        | REST
        | ARITY
    '''

def p_empty(p):
     'empty :'
     pass

def p_MultiDef(p):
    '''
    MultiDef : Def
            | Def MultiDef
    '''
def p_error(p):
    if p:
        print(f"Syntax error at token [{p.type} : {p.value}]")
        
    else:
        print('Error at EOF')

parser = yacc.yacc()


# FOR TESTING WITHOUT TESTING LEX
# if __name__ == '__main__':

#     with open('tests/test','r') as test:
#         parser.parse(test.read())  