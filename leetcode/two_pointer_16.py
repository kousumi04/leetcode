class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        res=nums[0]+nums[1]+nums[2]
        max_diff=float('inf')
        for i in range(0, n-2):
            left=i+1
            right=n-1
            # sum=-1*nums[i]
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==target:
                    return target
                    
                elif s<target:
                    left+=1
                else:
                    right-=1
                diff= abs(s-target)
                if diff<max_diff:
                    res=s
                    max_diff=diff
        return res              
s=Solution()
nums = [0, 0, 0]
target=2
print(s.threeSumClosest(nums, target))                                