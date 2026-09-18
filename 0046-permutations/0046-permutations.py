class Solution:

    def solve(self, subset, nums, res):
        if len(subset) == len(nums):
            res.append(subset.copy())
            return

        for num in nums:
            if num not in subset:
                subset.append(num)
                self.solve(subset, nums, res)
                subset.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.solve([], nums, res)
        return res