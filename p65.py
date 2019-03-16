n=int(input())
k=list(map(int,input().split()))
for i in range(0,len(k)):
    if k[i]<n:
        print(k[i],end=' ')
