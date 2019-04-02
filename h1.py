n=input()
a=list(map(int,input().split()))
r=[]
for i in range(0,len(a)):
    k=i+1 
    for j in range(k,len(a)):
        if a[i]==a[j] and a[i] not in r:
            r.append(a[i])
            s=sorted(r)
print(*s)
