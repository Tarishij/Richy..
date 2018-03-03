operator=["+","-","*","/","//","**","<<","%",">>"]
assignment=['=']
keyword=["Start",'is','Int','if','print','else','else_if','while','break','return']
delimiter=['{','}','(',')']
symbol=[";"]
identifier=['a','b','c','d','f']
relational_operator=['>','<','<=','>=','==','!=']
f=open("pm.txt","r")
l=f.read()
s=l.split("\n")
print(s)
length=len(s)
#splitted in lines 
for i in range (0,length):
    b=1
    a1=0
    for k in range(0,10):
        print(s[i])
        if keyword[k] in s[i]:
            print(keyword[k])
            print(keyword[k],"is keyword")
            a1=1
            break
    if(a1==1):
        continue
    p=list(s[i])
    length1=len(p)
    for j in range (0,length1):
        a1=0
        if(p[j]=='<'):
            print("<< is operator")
            a1=1
            j=j+2
             
        elif(p[j]=='>'):
            print(">> is operator")
            a1=1;j=j+2
        else:
            for k in range (0,4):
                if(p[j]==delimiter[k]):
                    print(p[j],"is delimiter")
                    a1=1
                    break
            if(a1==1):
                continue
            for k in range (0,5):
                if(p[j]==identifier[k]):
                    print(p[j],"is identifier")
                    a1=1
                    break
            if(a1==1):
                continue
         
            for k in range(0,9):
                if(p[j]==operator[k]):
                    if(p[j+1]==p[j]):
                        j=j+1
                        a1=1
                        print(p[j]*2,"is operator")
                        break
                    else:
                        a1=1
                        print(p[j],"is operator")
                    break
            if(a1==1):
                continue
            for k in range(0,2):
                if(p[j]==relational_operator[k]):
                    if(p[j+1]=='='):
                        print(p[j],"= is relational operator")
                        a1=1
                        break
                    else:
                        print(p[j],"is relational operator")
                        a1=1
                        break
     
            if(a1==1):
                continue
            
           
            if(p[j]=='='):
                if(p[j-1]=='!'):
                    print(p[j-1],"= is relational operator")
                    a1=1
                if(p[j-1]=='='):
                    print(p[j-1],"= is relational operator")
                    a1=1
                else:
                    print(p[j],"    assignment operator")
                    a1=1
            if(a1==1):
                continue 
            for k in range(0,1):
                if(p[j]==symbol[k]):
                    print(p[j],"is symbol");b=0
                    break   
            if(b==0):
                break
            
           
            if(p[j]>='0' or p[j]>='1'or p[j]>='2'or p[j]>='3'or p[j]>='4'or p[j]>='5'or p[j]>='6'or p[j]>='7'or p[j]>='8'or p[j]>='9'):
                print(p[j],"is constant")
    if(b==0):
        continue        
f.close()
