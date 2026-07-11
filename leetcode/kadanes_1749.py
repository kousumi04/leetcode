class Solution:
    def maxAbsoluteSum(self, nums):
        i=0
        minend=nums[i]
        maxend=nums[i]
        res=abs(nums[i])
        for i in range(1, len(nums)):
            v1=nums[i]
            v2=minend+nums[i]
            v3=maxend+nums[i]
            maxend=max(v1,v3)
            minend=min(v1,v2)
            res=max(res, abs(maxend), abs(minend))
        return res    
    
s=Solution()
nums=[1,-3,2,3,-4]
print(s.maxAbsoluteSum(nums))