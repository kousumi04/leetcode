class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)  
        res, sol=[],[]
        def solve():
            if len(sol)==n:
                res.append(sol[:])
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    solve()    
                    sol.pop()
        solve()
        return res            