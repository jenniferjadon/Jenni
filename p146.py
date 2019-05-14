b,d=map(int,input().split())
f=1 
g=1
while b>0:
    f=f*b
    b=b-1
while d>0:
    g=g*d
    d=d-1
n=f//g
print(n)
    
