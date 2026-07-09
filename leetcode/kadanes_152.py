# class Solution:
#     def maxProduct(self, nums):
#         i=0
#         best=nums[i]
#         low=nums[i]
#         ans=nums[i]
#         for i in range(1, len(nums)):
#             v1=best*nums[i]
#             v2=nums[i]
#             best=max(v1,v2)
#             ans=max(ans, best)
#         return ans    
# s=Solution()
# nums=[-2,3,-4]
# print(s.maxProduct(nums))