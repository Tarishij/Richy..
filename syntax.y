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
%token CONST ID WHILE BREAK RETURN RELOP
%token IF IS ELSE PRINT INT START END
%token INTEGER FLOAT FLOAT_VALUE
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
stmt : INT ID ';'  ID ASSIGNMENT int_expr
       |FLOAT ID ';'   ID ASSIGNMENT float_expr
       |print_stmt
       |iteration_stmt
       |break_stmt
       |return_stmt
       ;

print_stmt : PRINT'('ID',' SYMBOL ID ID SYMBOL ',' ID ',' ID')'
            |PRINT'('ID')'
            ;
if_stmt : IF'('cond')''{'stmt_list'}'                %prec "then"
          |IF'('cond')''{'stmt_list'}'ELSE'{'stmt_list'}'

          ;
cond  :ID IS INT
       |ID RELOP int_expr
       |ID RELOP float_expr
       |ID
       ;
iteration_stmt :WHILE'('cond')''{'stmt_list'}'
;
break_stmt:BREAK
;
return_stmt:RETURN
           |RETURN int_expr
           |RETURN float_expr
           ;
int_expr  : int_expr'+'int_term
      |int_expr'-'int_term
       |int_term
       |FLOOR int_id
        |CEIL int_id
        |ROOT int_id
        ;
float_expr  : float_expr'+'float_term
      |float_expr'-'float_term
       |float_term
       |FLOOR float_id
        |CEIL float_id
        |ROOT float_id
      ;
int_term : int_term '*' int_factor
       | int_term '/' int_factor
       |int_term '%' int_factor
       |ID POW int_factor
       |int_factor
       ;
float_term : float_term '*' float_factor
       | float_term '/' float_factor
       |float_term '%' float_factor
       |ID POW float_factor
       |float_factor
       ;
int_factor :'('int_expr')'       %prec "t"

        |INTEGER
        |int_id
        ;
float_factor :'('float_expr')'       %prec "t"

        |FLOAT_VALUE
        |float_id
        ;
int_id : ID ;

float_id : ID ;
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
	printf("Syntax error in line %d\n%s", line_no,s);
	exit(-1);
}

