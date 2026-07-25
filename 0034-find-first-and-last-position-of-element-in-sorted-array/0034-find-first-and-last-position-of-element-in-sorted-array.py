class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lowerBound():
            lb = -1
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return lb

        def upperBound():
            ub = -1
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ub = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ub

        lb = lowerBound()

        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        return [lb, upperBound()]