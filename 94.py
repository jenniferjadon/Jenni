a,b=map(int,input().split())
c=[int(i) for i in input().split()]
d=0
for r in range(0,len(c)):
    if c[r]==b:
        print(c[r])
