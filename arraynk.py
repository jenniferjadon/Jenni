
b,c=map(int,input().split())
t=[int(i) for i in input().split()]
if b>=c:
	s=[]
	for i in range (0,c):
		s.append(t[i])
	print(sum(s))
