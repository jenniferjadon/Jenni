k=int(input())
m=list(str(k))
c=0
for i in range(0,len(m)):
    for j in range(i+1,len(m)):
        if m[i]==m[j]:
            c=c+1 
if c>0:
    print("yes")
else:
    print("no")
