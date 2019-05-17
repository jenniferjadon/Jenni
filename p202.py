j=input()
d=[]
l=[]
for i in range(0,len(j)):
    if j[i]=='a' or j[i]=='e' or j[i]=='i' or j[i]=='o' or  j[i]=='u' or j[i]=='A' or j[i]=='E' or j[i]=='I' or j[i]=='O' or j[i]=='U':
        d.append(j[i])
    else:
        l.append(j[i])
s=d+l
for i in s:
    print(i,end='')
