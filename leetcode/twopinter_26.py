class Solution:
    def removeDuplicates(self, nums):
        i=1
        lst=[]
        while i<len(nums):
            # check if current value is equal to the previous value or not
            if nums[i]==nums[i-1]:
                # if found then remove
                n=nums.pop(i-1)
            else:
                i+=1  

        return len(nums)
nums=[0,0,1,1,1,2,2,3,3,4]
s=Solution()
print(s.removeDuplicates(nums))