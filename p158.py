n,p=map(int,input().split())
k=n*p
s=bin(k)
w=[]
for  i in range(0,len(s)):
    if s[i]=="1":
        w.append(i-1)
print(w[1])
