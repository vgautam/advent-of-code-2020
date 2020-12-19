%option noyywrap
%{
#include <stdio.h>
#include "y.tab.h" /* yacc symbol table, perhaps? */
%}

%%
a     return _4;
b     return _5;
\n    return NEWLINE;
%%
