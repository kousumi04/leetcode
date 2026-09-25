class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i=0
        best=nums[i]
        res=nums[i]
        for i in range(1, len(nums)):
            v1=best+nums[i]
            v2=nums[i]
            best=max(v1, v2)
            res=max(res,best)
        return res    