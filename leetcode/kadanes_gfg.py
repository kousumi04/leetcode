class Solution:
    def smallestSumSubarray(self, A):
        i=0
        low=A[i]
        ans=A[i]
        for i in range(1, len(A)):
            v1=low+A[i]
            v2=A[i]
            low=min(v1,v2)
            ans=min(ans, low)
        return ans
s=Solution()
nums=[3,-4, 2,-3,-1, 7,-5]
print(s.smallestSumSubarray(nums))