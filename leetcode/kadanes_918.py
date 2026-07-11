class Solution:
    def maxSubarraySumCircular(self, nums):
        curMin, curMax=0, 0
        globalMin, globalMax=nums[0], nums[0]
        res=0
        for i in nums:
            curMax=max(curMax+i, i)
            curMin=min(curMin+i, i)
            res+=i
            globalMax=max(globalMax,curMax)
            globalMin=min(globalMin,curMin)
        return max(globalMax, res-globalMin) if globalMax>0 else globalMax
s=Solution()
nums=[5, -3, 5] 
print(s.maxSubarraySumCircular(nums))  
        