n=int(input())
arr=list(map(int, input().split()))
i=1
freq=0
for i in range(len(arr)):
    if arr[i-1]>=arr[i]:
        freq+=1
print(freq)        