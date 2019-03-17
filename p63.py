n=int(input())
h=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(0,len(h)):
    for j in range(0,len(m)):
        if h[i]==m[j]: 
            print(m[j],end=' ')
        else:
            break
            
            
