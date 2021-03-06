%option noyywrap
%{
#include <stdio.h>
#include "y.tab.h" /* yacc symbol table, perhaps? */
%}

%%
[0-9]+	{ yylval.number=atol(yytext); return NUM; }
\(	return OPEN_PAREN;
\)	return CLOSE_PAREN;
\+	return ADD;
\*	return MUL;
\n	return NEWLINE;
[\t ]	; /* ignore other whitespace */
%%
