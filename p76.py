h=int(input())
f=list(map(int,input().split()))
s=[]
r=[]
for i in f:
    if i%2==0:
        s.append(i)
    else:
        r.append(i)
if len(s)==1:
    print(*s)
else:
    print(*r)
       
