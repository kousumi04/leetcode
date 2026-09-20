class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            prev = -1
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                # skip duplicate choices at same level
                if nums[j] == prev:
                    continue
                used[j] = True
                prev = nums[j]
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0, k, 0)