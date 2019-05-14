p=int(input())
for i in range(0,p):
    if 2**i==p:
        print("yes")
        break
else:
    print("no")
