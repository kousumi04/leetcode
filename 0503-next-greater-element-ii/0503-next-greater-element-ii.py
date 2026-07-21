class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n = len(nums)
        ans=[-1]*n
        for i in range(2*n):
            curr=nums[i%n]
            while stack and curr>nums[stack[-1]]:
                idx=stack.pop()
                ans[idx]=curr
            if i<n:
                stack.append(i)
        return ans    