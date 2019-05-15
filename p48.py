n=int(input())
s=[]
for  i in range(1,n+1):
    if  n%i==0:
        s.append(i)
for i in range(0,len(s)):
    if s[i]%2==1:
        print(s[i],end=" ")
