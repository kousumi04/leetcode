s=list(map(int, input().split()))
i=1
while i<len(s):
    if s[i-1]==s[i]:
        s.pop(i-1)
    else:
        i+=1
print(s)            