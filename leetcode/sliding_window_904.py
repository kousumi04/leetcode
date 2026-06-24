class Solution:
    def totalFruit(self, fruits):
        n=len(fruits)
        low=0
        freq={}
        res=0
        for high in range (n):
            fruit=fruits[high]
            freq[fruit]=freq.get(fruit,0)+1
            
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    freq.pop(fruits[low])
                low+=1
            res=max(res, high-low+1)
        return res  

s=Solution()
fruits=[1,2,1]
print(s.totalFruit(fruits))        