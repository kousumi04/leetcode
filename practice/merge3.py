def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    left=merge_sort(arr[:len(arr)//2])
    right=merge_sort(arr[len(arr)//2:])

    i=j=0
    k=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            k.append(left[i])
            i+=1

        else:
            k.append(right[j])
            j+=1

    k.extend(left[i:])
    k.extend(right[j:])

    return k

arr=[3, 4, 1, 7, 6, 9, 2, 8]
print(merge_sort(arr))