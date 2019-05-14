n=int(input())
h=bin(n)[2:]
c=0
for i in h:
    if i=='1':
        c=c+1
print(c)
