%option noyywrap
%{
#include <stdio.h>
#include "y.tab.h" /* yacc symbol table, perhaps? */
%}

%%
a     return _29;
b     return _114;
\n    return NEWLINE;
%%
