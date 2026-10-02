class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #-4, -1, -1, 0, 1, 2
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
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1                  
        return res           