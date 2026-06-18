class Solution:
    def removeDuplicates(self, nums):
        i=2
        while i<len(nums):
            if nums[i]==nums[i-1] and nums[i]==nums[i-2]:
                n=nums.pop(i-2)
            else:
                i+=1
        return len(nums)

s=Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))                
        