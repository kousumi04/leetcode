n=int(input())
temp=n
digs=len(str(n))
s=0
while temp>0:
    digits=temp%10 #last digit
    s+=digits**digs
    temp//=10
if s==n:
    print("Armstrong number")
else:
    print("nah it's not")        
