n=input().split()
c=0
for i in n:
    if i== "+" or "!" or "]" or "<" or ">" or "/" or "%" or "." :
        c=c+1
        print(c)
