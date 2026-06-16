class Solution:
    def sortedSquares(self, nums):
        size=len(nums)
        pos = []
        neg = []
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)

        # Case 1: No negative numbers 
        if len(neg)==0:
            return [x*x for x in pos]
        # Case 2: No positive numbers 
        if len(pos)==0:
            res=[x*x for x in neg]
            res.reverse()
            return res
        # Case 3: Both exists
        neg=[x*x for x in neg][::-1]
        pos=[x*x for x in pos]
        n,m=len(neg), len(pos)
        i=j=0
        res=[]
        
        while i<n and j<m:
            if neg[i]<=pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        while i<n:
            res.append(neg[i])
            i+=1        
        while j<m:
            res.append(pos[j])
            j+=1
        return res                

nums = [-4, 0, 1, 2, 3]
s = Solution()
print(s.sortedSquares(nums))  