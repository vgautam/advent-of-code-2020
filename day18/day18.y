%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int yylex(void);
int yyparse(void);
extern int yylineno, yychar;

void yyerror(const char *str)
{
    printf("%s: line %d, token %d\n", str, yylineno, yychar);
}

long long sum = 0;

int main()
{
    yyparse();
}
%}

%token OPEN_PAREN CLOSE_PAREN ADD MUL NEWLINE
%left	MUL
%left	ADD

%union
{
    long long number;
}

%token <number> NUM;
%type <number> expr;
%type <number> problem;
%%

homework:
    | problem homework
    {
        long long answer = $1;
        /* printf("%lld\n", answer); */
        sum += answer;
        printf("%lld\n", sum);
    }
    ;

problem:
    expr NEWLINE { $$ = $1; }
    ;

expr:
    OPEN_PAREN expr CLOSE_PAREN { $$ = $2; }
    | expr MUL expr { $$ = $1 * $3; }
    | expr ADD expr { $$ = $1 + $3; }
    | NUM { $$ = yylval.number; }
    ;

%%
