n=int(input())
h=list(map(int,input().split()))
c=0
for i in range(0,len(h)):
    if h[i]==h[i+1]:
        c=c+1 
        print(c)
    
