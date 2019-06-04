a,b=list(map(int,input().split()))
f=list(map(int,input().split()))
s=list(map(int,input().split()))
for i in s:
    f.append(i)
    m=max(f)
    print(m,end=' ')
