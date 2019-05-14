b,n=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
temp=0
for i in range(0,len(k)):
    if k[i]==n:
        c=c+1 
if c==0:
    print("no")
else:
    print("yes",c)

