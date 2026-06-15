def bubble_sort(arr):
    n=len(arr)

    for j in range(n-1):
        swapped=False
        for i in range(n-1-j):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swapped=True
        if not swapped:
            break        

if __name__=='__main__':
    arr=[5,9,2,1,67,34,88,34]
    bubble_sort(arr)
    print(arr)


