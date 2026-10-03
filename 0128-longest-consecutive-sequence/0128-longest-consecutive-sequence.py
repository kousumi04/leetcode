class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet=set(nums)
        # longest=0
        # for n in numSet:
        #     if n-1 not in numSet:
        #         length=1
        #         while n+length in numSet:
        #             length+=1
        #         longest=max(longest, length)
        # return longest     
        nums.sort()
        if not nums:
            return 0
        longest=1
        cur=1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                cur+=1
            else:
                cur=1
            longest=max(longest, cur)
        return longest         