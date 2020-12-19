%{
#include <stdio.h>
#include <string.h>

int yylex(void);
int yyparse(void);

void yyerror(const char *str)
{
   printf("error: %s\n", str);
}

int main()
{
    yyparse();
}

%}

%token _4 _5 NEWLINE

%%

_0: _4 _1 _5 NEWLINE { printf("success\n"); };

