class Solution:
    def maxProduct(self, nums):
        i=0
        maxend=nums[i]
        minend=nums[i]
        ans=nums[i]
        for i in range(1, len(nums)):
            v1=nums[i]
            v2=minend*nums[i]
            v3=maxend*nums[i]
            maxend=max(v1,max(v2,v3))
            minend=min(v1,min(v2,v3))
            ans=max(ans, max(maxend,minend))
        return ans    
s=Solution()
nums=[-2,3,-4]
print(s.maxProduct(nums))