n,k=map(int,input().split())
t=[]
h=list(map(int,input().split()))
for i in h:
    if i<k:
        t.append(i)
        s=sorted(t)
print(*s)
    
        
