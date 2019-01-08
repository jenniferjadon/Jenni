p=int(input())
count=0
while p>0:
	d=p%10
	count=count+1
	p=p//10
print(count)
