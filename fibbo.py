n=int(input())
i=1
first=0
second=1
while i<=n:
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)
    i=i+1
