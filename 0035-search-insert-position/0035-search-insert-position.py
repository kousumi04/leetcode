class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb=len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb            