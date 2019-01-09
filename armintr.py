n=int(input())
m=int(input())
s=0
temp=n
for i in range(n+1,m):
	while temp>0:
		digit=temp%10
	    s+=digit**3
	    temp=temp//10
if n==s:
	print(i)
