from bisect import bisect_left, insort
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        window=[]
        l=0
        for r in range(len(nums)):
            if r-l>indexDiff:
                pos=bisect_left(window, nums[l])
                window.pop(pos)
                l+=1
            pos=bisect_left(window, nums[r]-valueDiff)
            if pos<len(window) and window[pos]<=nums[r]+valueDiff:
                return True    
            insort(window, nums[r])    
        return False
