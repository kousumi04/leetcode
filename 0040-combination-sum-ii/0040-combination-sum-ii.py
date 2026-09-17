class Solution:
    def solve(self, start, total, subset, nums, target, res):
        if total==target:
            res.append(subset.copy()) 
            return
        if total>target:
            return
        for i in range(start, len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            self.solve(i+1, total+nums[i], subset, nums, target, res) 
            subset.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res=[]
        self.solve(0, 0, [], candidates, target, res)
        return res