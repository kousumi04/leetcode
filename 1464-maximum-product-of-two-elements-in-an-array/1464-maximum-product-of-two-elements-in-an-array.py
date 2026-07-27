class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        maximum=0
        n=len(nums)
        i=n-2
        j=n-1
        while i<j:
            return max((nums[i]-1)*(nums[j]-1), maximum)