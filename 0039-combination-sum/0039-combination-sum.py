class Solution:
    def solve(self, i, total, subset, candidate, target, res):
        if total==target:
            res.append(subset.copy())
            return
        elif total>target:
            return
        if i>=len(candidate):
            return

        s=total+candidate[i]  
        subset.append(candidate[i])
        self.solve(i,s, subset, candidate, target, res)
        e=subset.pop()
        s-=e
        self.solve(i+1,s, subset, candidate, target, res)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        self.solve(0, 0, [], candidates, target, res)  
        return res

