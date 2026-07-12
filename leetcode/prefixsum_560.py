class Solution:
    def subarraySum(self, nums, k):
        res=0
        curSum=0
        prefixSum={0:1}
        for i in nums:
           curSum+=i
           diff=curSum-k
           res+=prefixSum.get(diff,0)
           prefixSum[curSum]=prefixSum.get(curSum,0)+1
        return res    

s=Solution()
nums=[1,1,1]
print(s.subarraySum(nums,2))        
        