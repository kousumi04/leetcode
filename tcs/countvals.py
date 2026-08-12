s=input()
if not s:
    print("invalid")
else:
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    non="None"
    for ch in s:
        if freq[ch]==1:
            non=ch
            break
    most=s[0]
    for ch in s:
        if freq[ch]>freq[most]:
            most=ch
    print(non, most)        
