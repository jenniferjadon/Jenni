m=int(input())
for i in range(0,m+1):
	if(2**i)==m:
		print("yes")
		break
else:
	print("no")
