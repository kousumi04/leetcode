
def quicksort(arr, l, r):
    if l<r:
    
        parti=partition(arr, l, r)
        quicksort(arr, l, parti-1)
        quicksort(arr, parti+1, r)

def partition(arr, l, r):
    i=l
    j=r-1
    pivot=arr[r]

    while i<j:
        while i<r and arr[i]<pivot:
            i+=1
        while j>l and arr[j]>=pivot:
            j-=1

        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

    if arr[i]>pivot:
        temp=arr[i]
        arr[i]=arr[r]
        arr[r]=temp           

    return i   


arr=[22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr)-1)
print(arr)