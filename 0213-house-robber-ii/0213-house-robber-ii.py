class Solution:
    def solve(self,num):
        n=len(num)
        dp=[-1]*n
        dp[0]=num[0]
        for i in range(1,n):
            if i>1:
                pick=num[i]+dp[i-2]
            else:
                pick=num[i]
            not_pick=0+dp[i-1]
            dp[i]=max(pick, not_pick)
        return dp[n-1]        

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        ans1=self.solve(nums[0:n-1])
        ans2=self.solve(nums[1:n])
        return max(ans1, ans2)