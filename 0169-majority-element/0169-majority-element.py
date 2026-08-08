class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        res, majority=0,0
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>majority:
                res=i
                majority=freq[i]
        return res         
