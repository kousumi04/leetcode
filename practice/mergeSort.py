def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])

    i=0
    j=0
    sorted=[]
    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1

    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

arr=[13, 5, 4, 3, 9, 2, 16, 7, 4]
print(mergeSort(arr))        