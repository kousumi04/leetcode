class Solution:
    def maxSubarraySum(self, arr, k):
        if len(arr)<k:
            return 0
        max_sum=sum(arr[:k])
        res=max_sum
        for i in range(k,len(arr)):
            max_sum+=arr[i]-arr[i-k]
            res=max(res, max_sum)
        return res     
s=Solution()
arr=[100, 200, 300, 400]
k=2
print(s.maxSubarraySum(arr,k))