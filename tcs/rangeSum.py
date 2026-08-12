# i=int(input())
# j=int(input())
# if i>=j or i<0 or j>=10000:
#     print("Invalid input i & j.")
# else:
#     s=(j*(j+1)/2)-(i*(i-1)/2)
# print(s)   
# 

i=int(input())
j=int(input())
s=0
if i>=j or i<0 or j>=10000:
    print("Invalid input i & j.")
for k in range(i, j+1):
    s+=k
print(s)    

