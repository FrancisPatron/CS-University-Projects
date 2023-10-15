import sys
from Parser import parser 
from pprint import pprint

test_file = 'python lexer&parser for CICOM/tests/test'

def main():
    with open(test_file,'r') as input_file:
        parser.parse(input_file.read())
        print('If you only see this -> No Errors')

if __name__ == '__main__' :
    main() 