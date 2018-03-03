%{
#include<stdio.h>
FILE *fp;
%}
digit         [0-9]
letter        [a-zA-Z]
%%
"Start"                {fprintf(fp,"%s - keyword\n",yytext);}

"if"                   {fprintf(fp,"%s - keyword\n",yytext);}
"Int"                  {fprintf(fp,"%s - keyword\n",yytext);}
"Float"                  {fprintf(fp,"%s - keyword\n",yytext);}
"print"                {fprintf(fp,"%s - keyword\n",yytext);}
"else"                 {fprintf(fp,"%s - keyword\n",yytext);}
"while"                 {fprintf(fp,"%s - keyword\n",yytext);}
"break"                 {fprintf(fp,"%s - keyword\n",yytext);}
"return"                 {fprintf(fp,"%s - keyword\n",yytext);}
"("                    {fprintf(fp,"%s - delimiter\n",yytext);}
")"                    {fprintf(fp,"%s - delimiter\n",yytext);}
"{"                    {fprintf(fp,"%s - delimiter\n",yytext);}
"}"                    {fprintf(fp,"%s - delimiter\n",yytext);}
"="                    {fprintf(fp,"%s - assignment operator\n",yytext);}
";"                    {fprintf(fp,"%s - symbol\n",yytext);}
","                    {fprintf(fp,"%s - symbol\n",yytext);}
"**"                   {fprintf(fp,"%s - operator\n",yytext);}
"#"                   {fprintf(fp,"%s - operator\n",yytext);}
"+"                    {fprintf(fp,"%s - operator\n",yytext);}
"-"                    {fprintf(fp,"%s - operator\n",yytext);}
"*"                    {fprintf(fp,"%s - operator\n",yytext);}
"/"                    {fprintf(fp,"%s - operator\n",yytext);}
"%"                    {fprintf(fp,"%s - operator\n",yytext);}
"<<"                   {fprintf(fp,"%s - floor\n",yytext);}
">>"                   {fprintf(fp,"%s - ceil\n",yytext);}
"<"|">"|"<="|">="|"=="|"!="   {fprintf(fp,"%s - relational\n",yytext);}
"End"                  {fprintf(fp,"%s - keyword\n",yytext);}
["]                    {fprintf(fp,"%s - symbol\n",yytext);}
{letter}({letter}|{digit})*  {fprintf(fp,"%s - identifier\n",yytext);}
{digit}+|-{digit}+ 				{fprintf(fp,"%s - integer\n",yytext);}
{digit}+"."{digit}*|-{digit}+"."{digit}* 	  {fprintf(fp,"%s - float\n",yytext);}
[ \t\n\r]                    /* skip whitespace */

%%

int main(int argc,char **argv)
{

	yyin=fopen("pm.txt","r");
fp=fopen("a.txt","w");
	yylex();

	fclose(yyin);
	fclose(fp);
	return 0;
	fp=fopen("a.txt","w");
}

