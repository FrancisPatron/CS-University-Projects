'''
Created by: Francis J. Patrong Fidalgo, UPRM ICOM student

This code will print the regex in Jflex format for some lexical rules for the Scheme programming language
 '''

radixes = [2,8,10,16]

def num_gen():
    for r in radixes:
        print(f'num{r} = {{prefix{r}}}{{complex{r}}}')

def complex_gen():
    for r in radixes:
        print(f'complex{r} = {{real{r}}} | {{real{r}}}@{{real{r}}} | {{real{r}}}\+{{imag{r}}} | {{real{r}}}\-{{imag{r}}} | \+{{imag{r}}} | \-{{imag{r}}}')   

def imagr_gen():
    for r in radixes:
        print(f'imag{r} = i|{{ureal{r}}}i')

def realr():
    for r in radixes:
        print(f'real{r} = {{sign}}{{ureal{r}}}')

def ureal():
    for r in radixes:
        print(f'ureal{r} = {{uinteger{r}}} | {{uinteger{r}}} \/ {{uinteger{r}}} | {{decimal{r}}}')

def uinteger():
    for r in radixes:
        print(f'uinteger{r} = {{digit{r}}}+#*')

def prefix():
    for r in radixes:
        print(f'prefix{r} = {{radix{r}}}{{exactness}} | {{exactness}}{{radix{r}}}')


if __name__ == '__main__':
    num_gen()
    complex_gen()
    imagr_gen()
    realr()
    ureal()
    uinteger()
    prefix()