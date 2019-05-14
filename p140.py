n=input()
for i in range(0,len(n)):
    if n[i]!='a' and n[i]!='b':
        print("no")
        break
else:
    print("yes")
