n=int(input())
single=0
for _ in range(n):
    single^=int(input())
print(single)    

'''
1^1^2^3^3
___
 0^2^3^3
 ___
  2^3^3
    ____
   2 ^ 0 
    2
'''