b=int(input())
r=0
while b>0:
    rem=b%10
    r=(r*10)+rem
    b=b//10
print(r)
    
