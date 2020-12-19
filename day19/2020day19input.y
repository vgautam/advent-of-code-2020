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

%token _29 _114 NEWLINE

%%

_0: _8 _11 NEWLINE { printf("success\n"); };
