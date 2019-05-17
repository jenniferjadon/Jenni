n=int(input())
d=list(map(int,input().split()))
f=0
for i in range(0,len(d)-1):
    f=f+max(d[i],d[i+1])
print(f)
    
