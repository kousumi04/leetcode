class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        countOnes=0
        count=0
        for i in range(0, len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count=0
            countOnes=max(count, countOnes)
        return countOnes    