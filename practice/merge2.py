def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    
    sorted=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1    
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted
 
arr=[4,7,3,8,2,9,1,6]
arr=mergesort(arr)
print(arr)