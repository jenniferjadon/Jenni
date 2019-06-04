#jenni
import math
f,t=map(int,input().split())
c=0
for i in range(f,t+1):
    f=math.sqrt(i)
    if int(f+0.5)**2==i:
        c=c+1
print(c)
    
