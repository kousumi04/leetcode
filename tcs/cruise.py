# A party has been organised on cruise. The party is organised for a limited time(T). The number of guests entering (E[i]) and leaving (L[i]) the party at every hour is represented as elements of the array. The task is to find the maximum number of guests present on the cruise at any given instance within T hours.

# Example 1:

# Input :

# 5    -> Value of T
# [7,0,5,1,3]  -> E[], Element of E[0] to E[N-1], where input each element is separated by new line 
# [1,2,1,3,4]   -> L[], Element of L[0] to L[N-1], while input each element is separate by new line.


def cruise(n,E,L):
    total=0
    maximum=0
    for i in range(n):
        total=total+E[i]-L[i]
        
        maximum=max(maximum,total)
    return maximum

E=[7,0,5,1,3]
L=[1,2,1,3,4]
print(cruise(5,E,L))