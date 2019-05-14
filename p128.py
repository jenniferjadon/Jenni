k=int(input())
p=1
s=list(map(int,input().split()))
for i in range(0,len(s)):
    p=p*s[i]
    if p%2==0:
        print("even")
        break
else:
    print("odd")
    



  
