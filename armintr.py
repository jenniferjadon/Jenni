a,b=map(int,input().split())
x=' '
for n in range(a+1,b):
    s=0
    t=n
    while t>0:
        digit=t%10
        s=s+digit**3
        t=t//10
    if s==n:
        x=x+str(n)+' '
print(x.strip())
