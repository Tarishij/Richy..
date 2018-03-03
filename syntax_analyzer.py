operator=["+","-","*","/","//","**","<<","%",">>"]
assignment=['=']
keyword=["Start",'if','is','Int','print','else','else_if','while','break','return']
delimiter=['{','}','(',')']
symbol=[";"]
identifier=['a','b','c','d','f']
relational_operator=['>','<','<=','>=','==','!=']
f=open("pm.txt","r")
f2=open("symbol.txt","w")
l=f.read()
s=l.split("\n")
length=len(s)
#splitted in lines 
for i in range (0,length):
    b=1
    a1=0;a=0
    for k in range(0,10):
        if keyword[k] in s[i]:
            f2.write(keyword[k]+"-keyword\n")
  
            if(len(keyword[k])==len(s[i])):
                a=1
            break
    if a==1:
        continue
    
    p=list(s[i])
    length1=len(p)
    
    for j in range (0,length1):
        a1=0
        if(p[j]=='i' and p[j+1]=='s'):
            f2.write("is-keyword\n");a1=1;j=j+1
        if(p[j]=='I' and p[j+1]=='n' and p[j+2]=='t'):
            f2.write("Int-keyword\n");a1=1;j=j+2
        if(a1==1):
            continue
        if(p[j]=='"'):
            j=j+12
            continue
        if(p[j]==','):
            f2.write(p[j]+'-symbol\n');continue
        if(p[j]=='<'and p[j+1]==p[j]):
            f2.write("<<-operator\n")
            a1=1
            j=j+1
            continue
        elif(p[j]=='>'and p[j+1]==p[j]):
            f2.write(">>-operator\n")
            a1=1;j=j+1;continue
        else:
            for k in range (0,4):
                if(p[j]==delimiter[k]):
                    f2.write(p[j]+"-delimiter\n")
                    a1=1
                    break
            if(a1==1):
                continue
            for k in range (0,5):
                if(p[j]==identifier[k]):
                    if(p[j]=='f' and p[j-1]=='i'):
                        break
                    else:
                        f2.write(p[j]+"-identifier\n")
                        a1=1
                        break
            if(a1==1):
                continue
         
            for k in range(0,9):
                if(p[j]==operator[k]):
                    if(p[j+1]==p[j]):
                        j=j+1
                        a1=1
                        f2.write(p[j]*2+"-operator\n")
                        break
                    else:
                        a1=1
                        f2.write(p[j]+"-operator\n")
                    break
            if(a1==1):
                continue
            for k in range(0,2):
                if(p[j]==relational_operator[k]):
                    if(p[j+1]=='='):
                        f2.write(p[j]+"=-relational operator\n")
                        a1=1
                        break
                    else:
                        f2.write(p[j]+"-relational operator\n")
                        a1=1
                        break
     
            if(a1==1):
                continue
            
           
            if(p[j]=='='):
                if(p[j-1]=='!'):
                    f2.write(p[j-1]+"=-relational operator\n")
                    a1=1
                if(p[j-1]=='='):
                    f2.write(p[j-1]+"=-relational operator\n")
                    a1=1
                else:
                    f2.write(p[j]+"-assignment operator\n")
                    a1=1
            if(a1==1):
                continue 
            for k in range(0,1):
                if(p[j]==symbol[k]):
                    f2.write(p[j]+"-symbol\n");b=0
                    break   
           
            
           
            if(p[j]=='0' or p[j]=='1'or p[j]=='2'or p[j]=='3'or p[j]=='4'or p[j]=='5'or p[j]=='6'or p[j]=='7'or p[j]=='8'or p[j]=='9'):
                f2.write(p[j]+"-constant\n")
         
f.close()
f2.close()
f=open("symbol.txt","r") ;m=0
t=f.read()
l=t.split("\n")
m1=0
length=len(l)
s=l[0].split("-")
if s[0]!="Start":
    print("Error in line1:invalid beginning")
    m=1
s=l[1].split("-")
if s[0]!="{":
    print("Error: opening braces missing")
    m=1

s=l[length-2].split('-')

if s[0]!="}":
    print (s[0])
    print("Error: closing braces missing")
    m=1
for i in range(2,length-2):
    if "assignment_operator" in l[i]:
        if (not("identifier" in l[i-1])):
            print("Error: invalid assignment")
            m=1
    if ";" in l[i]:
        if not(("identifier" in l[i-1]) or ("constant" in l[i-1]) or (")" in l[i-1])):
            print("Error:invalid ending")
            m=1
    if "assignment_operator" in l[i]:
        if not(("constant" in l[i+1]) or ("identifier" in l[i+1]) or("operator" in l[i+1])):
            print("Error:invalid assignment")
            m=1
    if "print"  in l[i]:
        if not("(" in l[i+1]):
            print("Error:invalid output format")
            m=1
    if "if-" in l[i]:
        
        if not("(" in l[i+1]):
            print(l[i+1])
            print("Error:incorrect if statement")
            m=1
    if "{" in l[i]:
        if not((")" in l[i-1]) or ("else" in l[i-1])):
            print("Error:invalid condition statement")
            m=1
    if "}" in l[i]:
        if not(";" in l[i-1]):
            print("Error:missing semicolon")
            m=1
    if("," in l[i]):
        if not("identifier" in l[i+1] or "," in l[i+1] ):
            print("Error:in print")
            m=1
    if("constant" in l[i]):
        if not("operator" in l[i+1] or ";" in l[i+1] ):
            print("Error:missing ; at the end of the line")
            m=1
    if("operator" in l[i]):
        if not("**" in l[i] or "//"in l[i]  or "+" in l[i] or"-"in l[i] or"/"in l[i] or"%"in l[i] or"*"in l[i] or "<<"in l[i] or ">>"in l[i] ):
            print("Error: invalid operator")
            m=1
    if("(" in l[i]):
        while(not(")"in l[i+1] )and i+1<=length-2):
            i=i+1
            if(i==length-2):
                m1=1
        if(m1==1):

            print("Error:missing closing braces")
    if("{" in l[i]):
       while(i<=length-3 and not("}"in l[i+1] )):
           i=i+1
           if(i==length-3):
               m1=1
       if(m1==1):

           print("Error:missing closing braces")      
             
if(m!=1 and m1!=1):
    print("No Error")
f.close()
