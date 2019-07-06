n,m=list(map(int,input().split()))
d=m^n
f=bin(d)
c=0
for i in f:
    if i=="1":
        c=c+1 
print(c)
    
