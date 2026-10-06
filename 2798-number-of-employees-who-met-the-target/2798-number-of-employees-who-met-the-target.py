class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        count=0
        for h in hours:
            if h>=target:
                count+=1
        return count            