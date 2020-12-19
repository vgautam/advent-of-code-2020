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

%token NUM OPEN_PAREN CLOSE_PAREN ADD MUL NEWLINE

%%

homework:
    | problem homework
    ;

problem:
    expr NEWLINE
    ;

expr:
    OPEN_PAREN expr CLOSE_PAREN
    | expr MUL expr
    | expr ADD expr
    | NUM
    ;

%%
