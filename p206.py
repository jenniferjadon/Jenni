p=input()
c=0
g=[1-9]
for i in p:
    if i==g or i=='A' or i=='B' or i=='C' or i=='D' or i=='E' or i=='F':
        c=c+1 
if c==len(p):
    print("yes")
else:
    print("no")
        
