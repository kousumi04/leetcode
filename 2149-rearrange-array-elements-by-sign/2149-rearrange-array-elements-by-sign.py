class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg, pos=[], []
        res=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        n, p=len(neg), len(pos)
        j=0
        while j<n or j<p:
            if j<p:
                res.append(pos[j])
            if j<n:
                res.append(neg[j])    
            j+=1
        return res            

