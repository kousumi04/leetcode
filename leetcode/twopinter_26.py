class Solution:
    def removeDuplicates(self, nums):
        i=1
        lst=[]
        while i<len(nums):
            if nums[i]==nums[i-1]:
                n=nums.pop(i-1)
            else:
                i+=1  

        return len(nums)
nums=[0,0,1,1,1,2,2,3,3,4]
s=Solution()
print(s.removeDuplicates(nums))