f1=open("pm.txt","r")
d=0;e=0
l1=f1.read()
s1=l1.split("\n")
p1=s1[4].split( )
print(p1)
p2=s1[5].split( )
print(p2)
if p1[0]=="Int":
    e=1
    int_id=p1[1].split(",")
if p2[0]=="Float":
    d=1
    fo_id=p2[1].split(",")
print(int_id);print(fo_id)
f=open("a.txt","r")
l=f.read()
s=l.split("\n")
flag=0;r=0
length=len(s)
#splitted in lines
for i in range (0,length-1):
    p=s[i].split( )
    if p[0]=="=":
        p3=s[i-1].split( )
        if e==0:
            break
        else:
            m=len(int_id)
            for j in range (0,m):
                if(set(int_id[j])==set(p3[0])):

                    k=s[i+1].split( )
                    if(k[2]=="float"):
                        print("syntax error, unexpected FLOAT_VALUE")
                        flag=1
                    break
if(flag==0):
    r=1
flag=0
for i in range (0,length-1):
    p=s[i].split( )
    if p[0]=="=":
        p3=s[i-1].split( )
        if d==0:
            break
        else:
            n=len(fo_id)
            for j in range (0,n):
                if(set(fo_id[j])==set(p3[0])):
                    k=s[i+1].split( )
                    if(k[2]=="integer"):
                        print("syntax error, unexpected INT_VALUE")
                        flag=1
                    break
if(flag==0 and r==1):
    print("NO error\n")
f.close()
f1.close()
