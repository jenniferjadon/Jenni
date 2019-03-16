n,m=map(int,input().split())
k=list(map(int,input().split()))
for i in range(0,len(k)):
    if k[i]+k[i]==m:
        print("yes")
        break
    else:
        print("no")
        break
