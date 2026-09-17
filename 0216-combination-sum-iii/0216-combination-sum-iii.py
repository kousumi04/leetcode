class Solution:
    def solve(self, last, total, subset, target, k, res):
        if total==target and len(subset)==k:
            res.append(subset.copy())
            return
        if total>target or len(subset)>k:
            return

        for i in range(last,10):
            s=total+i
            subset.append(i)
            self.solve(i+1, s, subset, target, k, res)
            subset.pop()

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res=[]
        self.solve(1, 0, [], n, k, res)
        return res
        