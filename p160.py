n,m=map(int,input().split())
s=n|m
y=bin(s)
#print(s)
c=0
for i in range(0,len(y)):
    if  y[i]=="1":
        c=c+1 
print(c)
        
