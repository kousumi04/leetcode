

# using iteration

# def binarySearch(arr, target):
#     l=len(arr)
#     start=0
#     end=l-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if target>arr[mid]:
#             start=mid+1
#         elif target<arr[mid]:
#             end=mid-1 
#         else:
#             return mid
#     return -1    

# arr=[-1, 0, 3, 4, 5, 9, 12]
# target=9
# print(binarySearch(arr, target))


# using recursion
def binarySearch(arr, target, start, end):
    if start<=end:
        mid=start+(end-start)//2
        if target>arr[mid]:
            return binarySearch(arr, target, mid+1, end )
        elif target<arr[mid]:
            return binarySearch(arr, target, start, mid-1)   
        else:
            return mid
    return -1

arr=[-1, 0, 3, 4, 5, 9, 12]
target=9
start=0
end=6
print(binarySearch(arr, target, start, end))    