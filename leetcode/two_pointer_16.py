class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        max_diff=float('inf')
        for i in range(0, len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right] # sum of first three elements
                # best case
                if s==target:
                    return target
                    
                elif s<target:
                    left+=1
                else:
                    right-=1
                    # finding the difference or sum from target
                diff= abs(s-target)
                if diff<max_diff:
                    res=s
                    max_diff=diff
        return res              
s=Solution()
nums = [0, 0, 0]
target=2
print(s.threeSumClosest(nums, target))                                