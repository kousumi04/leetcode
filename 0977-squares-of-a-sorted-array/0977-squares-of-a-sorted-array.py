class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=len(nums)
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        if len(neg)==0:
            return [x*x for x in pos]
        elif len(pos)==0:
            res=[x*x for x in neg]
            res.reverse()
            return res
        else:
            neg=[x*x for x in neg][::-1] 
            pos=[x*x for x in pos]  
            n, p=len(neg), len(pos)
            i, j=0, 0
            res=[]
            while i<n and j<p:
                if neg[i]<=pos[j]:
                    res.append(neg[i])
                    i+=1
                else:
                    res.append(pos[j])
                    j+=1
            while i<n:
                res.append(neg[i])
                i+=1    
            while j<p:
                res.append(pos[j])
                j+=1
            return res