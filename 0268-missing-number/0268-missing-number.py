class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort() 
        total=0
        currSum=sum(nums)
        for i in range(len(nums)+1):
            total=total+i
        return total-currSum