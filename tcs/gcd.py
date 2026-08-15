n=int(input())
m=int(input())
while n>0 and m>0:
    if n>m:
        n=n%m
    else:
        m=m%n
if n==0:
    print(m)
else:
    print(n)                 