h=int(input())
k=[]
a=list(map(int,input().split()))
g=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(0,len(g)):
        if a[i]==g[j]:
            k.append(a[i])
for i in range(0,len(k)):
    print(k[i],end=" ")
