n=int(input())
k=1
while n!=0:
    c=n%10
    k=k*c
    n=n//10
print(k)
