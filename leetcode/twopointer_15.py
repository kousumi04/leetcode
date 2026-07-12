# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         n=len(nums)
#         result=[]
#         for i in range(0, n-2):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             left=i+1
#             right=n-1
#             sum=-1*nums[i]
#             while left<right:
#                 s=nums[left]+nums[right]
#                 if s==sum:
#                     result.append([nums[i], nums[left], nums[right]])
#                     left+=1
#                     right-=1
#                     while left<right and nums[left]==nums[left-1]:
#                         left+=1
#                     while left<right and nums[right]==nums[right+1]:
#                         right-=1
#                 elif s<sum:
#                     left+=1
#                 else:
#                     right-=1
#         return result
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i in range(0, len(nums)-2):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                if nums[i]+nums[j]+nums[k]==0: 
                    res.append([nums[i], nums[j], nums[k]]) 
                    j+=1
                    k-=1
                    # skip duplicate second element
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    # skip duplicate third element    
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1                  
        return res           
s=Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))                                