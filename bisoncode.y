%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern int yyparse();
extern FILE *yyin;
extern int line_no;
void yyerror(const char *s);

%}
%define parse.error verbose
%define parse.lac none
%token CONST ID
%token IF IS ELSE PRINT INT START END
%token ASSIGNMENT
%token SYMBOL
%token POW CEIL FLOOR ROOT
%nonassoc "then"
%nonassoc ELSE
%nonassoc CEIL FLOOR ROOT
%left  '+' '-'
%left  '*' '/'
%nonassoc "t"
%right POW
%%

S        :  START '{'stmt_list '}'END

          ;
stmt_list : stmt ';' stmt_list

          |if_stmt
          |stmt ';'



            ;
stmt : ID ASSIGNMENT expr
       |expr
       |if_stmt
       |print_stmt
       ;
print_stmt : PRINT'('ID',' SYMBOL ID ID SYMBOL ',' ID ',' ID')'
            |PRINT'('ID')'
;
if_stmt : IF'('cond')''{'stmt_list'}'                %prec "then"
          |IF'('cond')''{'stmt_list'}'ELSE'{'stmt_list'}'

          ;
cond  :

       ID IS INT
       ;

expr  : expr'+'term
      |expr'-'term
       |term
       |FLOOR ID
        |CEIL ID
        |ROOT ID
      ;
term : term '*' factor
       | term '/' factor
       |ID POW factor
       |factor
       ;
factor :'('expr')'       %prec "t"

        |CONST
        |ID
        ;


%%

int main()
{
	yyin=fopen("pm.txt","r");
	do
	{
		yyparse();
	} while (!feof(yyin));
	printf("All correct!\n");
}
void yyerror(const char *s)
{
	printf("Syntax error in line %d\n%s", line_no-1,s);
	exit(-1);
}
