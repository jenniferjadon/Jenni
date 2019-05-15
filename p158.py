n,p=map(int,input().split())
k=n*p
s=bin(k)
for  i in range(0,len(s)):
    if s[i]=='1':
        print(i+1)
        break
