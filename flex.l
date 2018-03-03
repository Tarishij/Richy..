%{
#include "y.tab.h"
#define YY_DECL extern int yylex()
int line_no = 1;
%}
digit         [0-9]
letter        [a-zA-Z]
%%
\n						{++line_no;}
"Start"                {return START;}
"is"                   {return IS;}
"if"                   {return IF;}
"Int"                  {return INT;}
"print"                {return PRINT;}
"else"                 {return ELSE;}
"while"                {return WHILE;}
"break"                {return BREAK;}
"return"               {return RETURN;}
"("|")"|"{"|"}"        {return yytext[0];}
"="                    {return ASSIGNMENT;}
";"                    {return yytext[0];}
","                   {return yytext[0];}
["]               {return SYMBOL;}
"**"                    {return POW;}
"#"                    {return ROOT;}
"+"|"-"|"*"|"/"        {return yytext[0];}
">"|"<"|"=="|"<="|">="|"!="    { return RELOP;}
"<<"                   {return FLOOR;}
">>"                   {return CEIL;}
"End"                  {return END;}
{letter}({letter}|{digit})*  {return ID;}
{digit}+                     {return CONST;}
[ \t\r]                    /* skip whitespace */

%%

