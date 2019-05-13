a,b=list(map(int,input().split()))
g=list(map(int,input().split()))
for i in range(0,len(g)):
    if g[i]==b:
        print("yes")
        break
else:
    print("no")
