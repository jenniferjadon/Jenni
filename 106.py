d,k=list(map(int,input().split()))
p=list(map(int,input().split()))
g=[]
for i in range(0,len(p)):
    if p[i]%2==1:
        g.append(p[i])
print(g[k-1])
    
