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
    a1=0;a=0;d=0

    
    p=list(s[i])
    length1=len(p)
    
    for j in range (0,length1):
        
        a1=0
        if(p[j]=='i' and p[j+1]=='f'):
            f2.write("if-keyword\n");a1=1;j=j+1
        if(j+4<=length1-1 and p[j]=='S' and p[j+1]=='t' and p[j+2]=='a' and p[j+3]=='r' and p[j+4]=='t'):   
            f2.write("Start-keyword\n");a1=1;j=j+4
        if(j+4<=length1-1 and p[j]=='p' and p[j+1]=='r' and p[j+2]=='i' and p[j+3]=='n' and p[j+4]=='t' ):   
            f2.write("print-keyword\n");a1=1;j=j+4
        if(j+3<=length1-1 and p[j]=='e' and p[j+1]=='l' and p[j+2]=='s' and p[j+3]=='e'):
            f2.write("else-keyword\n");a1=1;j=j+3
        
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


