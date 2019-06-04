i,r=map(int,input().split())
d=0
for j in range(i,r+1):
  k=2
  while k<=r:
    if j==k*k:
       d=d+1 
       break
    k=k+1
print(d)

