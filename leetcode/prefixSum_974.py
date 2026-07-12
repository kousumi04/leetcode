class Solution:
    def subarraysDivByK(self, nums, k):
        res=0
        prefixSum=0
        prefixC={0:1}
        for i in nums:
            prefixSum+=i
            rem=prefixSum%k
            res+=prefixC.get(rem,0)
            prefixC[rem]=prefixC.get(rem,0)+1    
        return res   
    
s=Solution()
nums=[4,5,0,-2,-3,1]
print(s.subarraysDivByK(nums, 5))    