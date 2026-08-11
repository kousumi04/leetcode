n=input()
days=int(input())
week={"mon":6, "tue":5, "wed":4, "thurs":3, "fri":2, "sat":1, "sun":0}
ans=0
if days-week[n]>1:
    ans=1+(days-week[n])//7
print(ans)    

