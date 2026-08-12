class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        # lst=[]
        while i<len(nums):
            if nums[i]==nums[i-1]:
                n=nums.pop(i-1)
            else:
                i+=1    
        return len(nums)