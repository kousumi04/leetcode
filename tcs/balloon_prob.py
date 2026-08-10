n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
freq={}
for ch in arr:
    freq[ch]=freq.get(ch, 0)+1

ans=""
for ch in arr:
    if freq[ch]%2!=0:
        ans=ch
        break
if ans:
    print(ans)
else:
    print("All are even.")        

