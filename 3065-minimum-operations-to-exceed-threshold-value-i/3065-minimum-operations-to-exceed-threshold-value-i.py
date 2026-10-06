class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort() #1 2 3 10 11
        count=0
        for n in nums:
            if n<k:
                count+=1
            else:
                break
        return count            
            