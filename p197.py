m=int(input())
f=list(map(int,input().split()))
k=sorted(f)
d=k[::-1]
e=d[0]-d[-1]
print(e)
