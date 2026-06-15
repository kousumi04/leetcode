
def quicksort(arr):
    if len(arr)<=1:
        return arr
    sorted_array=[]
    pivot=arr[0]
    
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]

    return quicksort(left)+[pivot]+quicksort(right)

arr=[3, 5, 91, 2, 4, 77, 82, 26]    
arr=quicksort(arr)
print(arr)