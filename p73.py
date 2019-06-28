h,m=list(map(int,input().split()))
f=list(map(int,input().split()))
for i in range(0,len(f)):
    if i==m:
        print(f.index(i)+1)
    
