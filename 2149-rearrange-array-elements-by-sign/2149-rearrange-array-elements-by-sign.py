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
        while j<len(neg) or j<len(pos):
            if j<len(pos):
                res.append(pos[j])
            if j<len(neg):
                res.append(neg[j])    
            j+=1
        return res            

