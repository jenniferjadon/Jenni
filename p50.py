n=int(input())
s=0
for i in range(1,n):
	if n%i==0:
		s=s+1	
if s>1:
	print("yes")
else:
	print("no")
	

