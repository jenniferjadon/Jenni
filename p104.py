n=int(input())
d=list(map(int,input().split()))
f=0
for i in range(0,len(d)-1):
    u=i+1
    f=f+(d[i]+d[u])
print(f)
    
