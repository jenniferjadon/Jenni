s=map(int,input().split())
d=list(map(int,input().split()))
h=list(map(int,input().split()))
k=h[::-1]
if k==d:
    print("yes")
else:
    print("no")
