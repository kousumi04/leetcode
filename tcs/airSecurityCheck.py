n=int(input())
arr=[]
a, b, c=0, 0, 0
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i==0:
        a+=1
    elif i==1:
        b+=1
    else:
        c+=1
arr.clear()
for i in range(a):
    arr+=[0]  
for i in range(b):
    arr+=[1]  
for i in range(c):
    arr+=[2] 
print(arr)                           