u=int(input())
u=str(u)
j=[]
for k in range(0,len(u)) :
    j.append(u[k])
f=sorted(j)
p=f[::-1]
for i  in p:
    print(i,end="")
