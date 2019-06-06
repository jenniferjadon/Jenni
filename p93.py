j=int(input())
d=list(map(int,input().split()))
for i in range(0,len(d)-1,2):
    d[i],d[i+1]=d[i+1],d[i]
print(*d)
    
