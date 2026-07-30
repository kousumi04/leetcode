class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high=0, len(nums)-1
        minimum=float('inf')
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<nums[high]:
                minimum=min(minimum, nums[mid])
                high=mid-1
            else:
                minimum=min(minimum, nums[low])
                low=mid+1
        return minimum                    