class Solution:
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(0, n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            sum=-1*nums[i]
            while left<right:
                s=nums[left]+nums[right]
                if s==sum:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif s<sum:
                    left+=1
                else:
                    right-=1
        return result

s=Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))                                