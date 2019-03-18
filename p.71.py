n=int(input())
m=list(map(int,input().split()))
for i in range(0,len(m)):
    if m[i]<=m[i+1]:
       print(m[i+1],end=' ')
        
