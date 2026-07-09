class Solution:
    def maxSubArray(self, nums):
        i=0
        best_ending=nums[i]
        ans=nums[i]
        for i in range(1,len(nums)):
            v1=best_ending+nums[i]
            v2=nums[i]
            best_ending=max(v1, v2)
            ans=max(ans,best_ending)
        return ans    
s=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))