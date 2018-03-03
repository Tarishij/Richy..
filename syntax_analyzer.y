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
%token FLOAT_VALUE INTEGER ID WHILE BREAK RETURN RELOP MAIN
%token IF ELSE PRINT INT START END FLOAT VOID
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

S        :  START  MAIN'{'stmt_list '}'END
          | START fun_decl1 MAIN '{'stmt_list fun_call1';' '}' fun_def1 END
            |START fun_decl2 MAIN '{'stmt_list fun_call2';' '}' fun_def2 END
           |START fun_decl3 MAIN '{'stmt_list fun_call3';' '}' fun_def3 END

          ;

fun_decl1  :type ID '('dec1')'';'
;
fun_decl2   :type ID '('dec2')'';'
;
fun_decl3   :type ID '('dec3')'';'
           ;
           
dec1 :   type
       
;
 dec2  :    type','type
     ;
dec3:    type ','type ','type
;
type   :    INT
           |FLOAT
           |VOID
           ;
stmt_list : stmt ';' stmt_list

          |if_stmt
          |int_decl stmt_list
       |float_decl stmt_list
          |stmt ';'
      ;
fun_def1 : type ID '('arg1')''{'stmt_list'}'
;
 fun_def2       :type ID '('arg2')''{'stmt_list'}'
 ;
 fun_def3      :type ID '('arg3')''{'stmt_list'}'
        ;
arg1     : type ID
         ;
arg2     : type ID ','type ID
         ;
arg3     : type ID ','type ID',' type ID
         ;
stmt : ID ASSIGNMENT expr

       |expr
       |print_stmt
       |iteration_stmt
       |break_stmt
       |return_stmt
       ;
fun_call1 :ID'('ID')'
          ;
fun_call2 :ID'('ID','ID')'
          ;
 fun_call3 :ID'('ID','ID','ID')'
          ;
int_decl:  INT int_id int_t
        ;
float_decl :FLOAT float_id float_t
            ;
int_t:  ','int_id int_t
         |
          ;
float_t: ','float_id float_t
            |
            ;
print_stmt : PRINT'('ID',' SYMBOL ID ID SYMBOL ',' ID ',' ID')'
            |PRINT'('ID')'
            | PRINT'(' SYMBOL ID ID SYMBOL','ID')'
;
if_stmt : IF'('cond')''{'stmt_list'}'                %prec "then"
          |IF'('cond')''{'stmt_list'}'ELSE'{'stmt_list'}'

          ;
cond  :ID ID INT
       |ID RELOP expr
       |ID
       ;
iteration_stmt :WHILE'('cond')''{'stmt_list'}'
;
break_stmt:BREAK
;
return_stmt:RETURN
           |RETURN expr
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
       |term '%' factor
       |ID POW factor
       |factor
       ;
factor :'('expr')'       %prec "t"

        |INTEGER
        |FLOAT_VALUE
        |ID
        ;
float_id:ID
;
int_id:ID
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
	printf("Syntax error in line %d\n%s", line_no,s);
	exit(-1);
}
