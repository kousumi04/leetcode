n=int(input()) # 10
k=int(input()) # 4
j=int(input()) # 3
m=int(input()) # 14
p=int(input()) # 9
bEaten=m/k
rem_banana=m%k
pEaten=p/j
rem_peanut=p%j
left=n-int((bEaten+pEaten))
if rem_banana!=0 or rem_peanut!=0:
    left=left-1

print(left)
# return 0