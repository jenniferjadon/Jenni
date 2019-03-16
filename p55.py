n,m=map(str,input().split())
if len(n)==len(m):
	if n.upper() or n.lower()==m.upper() or m.lower():
		print("yes")
else:
	print("no")
