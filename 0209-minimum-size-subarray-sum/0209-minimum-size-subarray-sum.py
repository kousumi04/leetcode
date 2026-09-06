class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        low=0
        res=float('inf')
        window_sum=0
        for high in range (n):
            window_sum+=nums[high]
            while window_sum>=target:
                res= min(res, high-low+1)
                window_sum-=nums[low]
                low+=1
        return 0 if res==float('inf') else res  