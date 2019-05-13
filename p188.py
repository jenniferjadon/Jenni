p=list(map(int,input().split()))
p=sorted(p)
if p[0]+p[1]>p[2]:
    print("yes")
else:
    print("no")
