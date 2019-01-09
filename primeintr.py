a=int(input())
b=int(input())
i=1
c=0
for i in range(a+1,b):
	if a%i==0:
		c=c+1
	i=i+1
print(i)
