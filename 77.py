num=int(input())
a=[]
for i in range(1,num+1):
    if num%i==0:
        a.append(i)
print (a)
