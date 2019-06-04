a,b=map(int,input().split())
input()
f=list(map(int,input().split()))
s=list(map(int,input().split()))
d=[]
for i in s:
    f.append(i)
    m=max(f)
    d.append(m)
print(*d)
