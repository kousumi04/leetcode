class Solution:
    def solve(self, start, subset, nums, res):
        res.append(subset.copy())
        
        for i in range(start, len(nums)):
            if i>start and nums[i]==nums[i-1] :
                continue
            subset.append(nums[i])
            self.solve(i+1, subset, nums, res)
            subset.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        # used=[False]*(len(nums))
        self.solve(0, [], nums, res)
        return res        