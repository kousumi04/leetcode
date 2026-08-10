# n=int(input())
# arr=list(map(int, input().split()))
# i=1
# freq=0
# for i in range(len(arr)):
#     if arr[i-1]>=arr[i]:
#         freq+=1
# print(freq)        



n=int(input())
arr=list(map(int, input().split()))
maximum=arr[0]
freq=1
for i in range(len(arr)):
    if maximum<arr[i]:
        freq+=1
        maximum=arr[i]
print(freq)        