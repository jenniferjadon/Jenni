n=int(input())
b=list(map(int,input().split()))
s=sorted(b)
if s==b:
	print("yes")
else:
	print("no")
