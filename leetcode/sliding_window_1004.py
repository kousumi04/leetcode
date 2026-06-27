class Solution:
    def longestOnes(self, nums, k):

        res=0
        left=0
        zeros=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1 
                #increments the count of zeros if present
            while zeros>k: #while the no. of 0s will be >k
                if nums[left]==0:
                    zeros-=1
                left+=1    
            res=max(res, right-left+1)
        return res
s=Solution()
nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k=3
print(s.longestOnes(nums, k))