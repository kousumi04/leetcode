arr=input() # ["*", "*", "*", "#", "#", "#"]
countStar=0
countHash=0
for ch in arr:
    if ch=="*":
        countStar+=1
    elif ch=="#":
        countHash+=1  
print(countStar-countHash)          