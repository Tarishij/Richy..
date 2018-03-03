%{

%}
digit         [0-9]
letter        [a-zA-Z]
%%
"Start"                {printf("%s - keyword\n",yytext);}
"is"                   {printf("%s - keyword\n",yytext);}
"if"                   {printf("%s - keyword\n",yytext);}
"Int"                  {printf("%s - keyword\n",yytext);}
"print"                {printf("%s - keyword\n",yytext);}
"else"                 {printf("%s - keyword\n",yytext);}
"("                    {printf("%s - delimiter\n",yytext);}
")"                    {printf("%s - delimiter\n",yytext);}
"{"                    {printf("%s - delimiter\n",yytext);}
"}"                    {printf("%s - delimiter\n",yytext);}
"="                    {printf("%s - assignment operator\n",yytext);}
";"                    {printf("%s - symbol\n",yytext);}
"**"                   {printf("%s - operator\n",yytext);}
"//"                   {printf("%s - operator\n",yytext);}
"+"                    {printf("%s - operator\n",yytext);}
"-"                    {printf("%s - operator\n",yytext);}
"*"                    {printf("%s - operator\n",yytext);}
"/"                    {printf("%s - operator\n",yytext);}
"%"                    {printf("%s - operator\n",yytext);}
","                    {printf("%s - symbol\n",yytext);}
"<<"                   {printf("%s - floor operator\n",yytext);}
">>"                   {printf("%s - ceil operator\n",yytext);}
"End"                  {printf("%s - keyword\n",yytext);}  
["]                    {printf("%s - symbol\n",yytext);}
{letter}({letter}|{digit})*  {printf("%s - identifier\n",yytext);}
{digit}+                     {printf("%s - constants\n",yytext);} 
[ \t\n\r]                    /* skip whitespace */  

%%

int main(int argc,char **argv)
{
	yyin=fopen("pm.txt","r");
	printf("Lexeme - Token\n");
	yylex();
	fclose(yyin);
	return 0;
}
