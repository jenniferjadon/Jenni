k=int(input())
for i in range(1,k):
	a=2**i
	if a==k:
		print("yes")
		break
else:
	print("no")
