n=int(input())
d=list(map(int,input().split()))
f=0
for i in range(0,len(d)):
    f=f+d[i]
    print(f,end=" ")
