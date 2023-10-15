/*
Francis J. Patron Fidalgo 802180833 2-1-2021 
Scheme lexical scanner
*/

%%
%class scheme_lex_scanner
%standalone
%line
%column

num           = {num2} | {num8} | {num10} | {num16}
startP        = \(
endP          = \)
comment       = ;.*{newline}
newline       = [\n]
empty         = ""
ws            = [\t\n]+  

constant      = {boolean} | {num} | {character} | {string}
formals       = {variable} | \({variable}*\) | \({variable}+\.{variable}\)
variable      = {id}
id            = {initial}{subsequent}*|\+|\-|\.\.\.
initial       = {letter}|\!|\$|%|&|\*|\/|:|<|  =|>|\?|\~|_|\^
subsequent    = {initial}|{digit}|\.|\+|-
letter        = [a-zA-Z]+
digit         = [0-9]+

boolean       = #t|#f
character     = #\\(.|{newline}|\s)
string        = \"{stringChar}*\"
stringChar    = \\\"|\\\\|[^\\\"]
keyword       =  acces|and|begin|bkpt|case|cond|cons-stream|declare|default-object\?|define(-integrable|-macro|-structure|-syntax)?
              |delay|do|fluid-test|if|in-package|lambda|let|let\*|let-syntax|letrec|local-declare|macro|make-enviorment|named-lambda|or
              |quasiquote|quote|scode-quote|sequence|set\!|the-enviroment|unassigned\?|using-syntax

djoint        = [a-z]+\?

num2          = {prefix2}{complex2}
num8          = {prefix8}{complex8}
num10         = {prefix10}{complex10}
num16         = {prefix16}{complex16}

complex2      = {real2} | {real2}@{real2} | {real2}\+{imag2} | {real2}\-{imag2} | \+{imag2} | \-{imag2}
complex8      = {real8} | {real8}@{real8} | {real8}\+{imag8} | {real8}\-{imag8} | \+{imag8} | \-{imag8}
complex10     = {real10} | {real10}@{real10} | {real10}\+{imag10} | {real10}\-{imag10} | \+{imag10} | \-{imag10}
complex16     = {real16} | {real16}@{real16} | {real16}\+{imag16} | {real16}\-{imag16} | \+{imag16} | \-{imag16}

imag2         = i|{ureal2}i
imag8         = i|{ureal8}i
imag10        = i|{ureal10}i
imag16        = i|{ureal16}i

real2         = {sign}{ureal2}
real8         = {sign}{ureal8}
real10        = {sign}{ureal10}
real16        = {sign}{ureal16}

ureal2        = {uinteger2} | {uinteger2} \/ {uinteger2} | {decimal10}
ureal8        = {uinteger8} | {uinteger8} \/ {uinteger8} | {decimal10}
ureal10       = {uinteger10} | {uinteger10} \/ {uinteger10} | {decimal10}
ureal16       = {uinteger16} | {uinteger16} \/ {uinteger16} | {decimal10}

uinteger2     = {digit2}+#*
uinteger8     = {digit8}+#*
uinteger10    = {digit10}+#*
uinteger16    = {digit16}+#*

prefix2       = {radix2}{exactness} | {exactness}{radix2}
prefix8       = {radix8}{exactness} | {exactness}{radix8}
prefix10      = {radix10}{exactness} | {exactness}{radix10}
prefix16      = {radix16}{exactness} | {exactness}{radix16}

decimal10     = {uinteger10}{exponent} | \.{digit10}+#*{suffix} | {digit10}+\.{digit10}*#*{suffix} | {digit10}+#+\.#*{suffix}
suffix        = {empty}|{exponent}
exponent      = {exponentMark}{sign}{digit10}+
exponentMark  = e|s|f|d|l
sign          = {empty}|\+|\-
exactness     = {empty}|#i|#e 
radix2        = #b
radix8        = #o
radix10       = {empty} | #d
radix16       = #x
digit2        = [0-1]
digit8        = [0-7]
digit10       = {digit}
digit16       = {digit}|[a-f]


%%
{empty}    {}
{ws}       {}
{startP}   {System.out.print("INITP["+yytext()+"]");}
{endP}     {System.out.print("ENDP["+yytext()+"]");}
{djoint}   {System.out.print("DJNT["+yytext()+"]");}
{num}      {System.out.print("NUM["+yytext()+"]");}
{keyword}  {System.out.print("KWRD[" + yytext()+"]");}
{id}       {System.out.print("ID["+ yytext()+"]");}
{comment}  {System.out.print("COMNT["+ yytext()+"]");}
{boolean}  {System.out.print("BOOL["+ yytext()+"]");}
{string}   {System.out.print("STR["+ yytext()+"]");}
{constant} {System.out.print("CONS["+ yytext()+"]");}
{formals}  {System.out.print("FRML["+ yytext()+"]");}