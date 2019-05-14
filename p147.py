g=input().split()
if len(g)==1 or len(g)==2:
    for i in range(0,len(g)):
        print(g[i],end=' ')
else:
    print(g[0],end=' ')
    for i in range(1,len(g)-1):
        k=g[i][::-1]
        print(k,end=' ')
    print(g[-1])

