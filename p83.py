n=int(input())
h=list(map(int,input().split()))
for i in range(0,len(h)):
    if n==1:
        print(h[i])
        break
    if h[i]!=h[i+1]:
        print(h[i]+h[i+1])
        break
    if h[i]==h[i+1]:
        print(h[i])
        break
