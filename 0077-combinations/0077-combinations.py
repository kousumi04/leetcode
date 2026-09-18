class Solution:
    def solve(self, i, subset, n, k, res):
        if len(subset)==k:
            res.append(subset.copy())
            return
        for i in range(i, n+1):
            subset.append(i)
            self.solve(i+1, subset, n, k, res)    
            subset.pop()
            
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        self.solve( 1, [], n, k, res)
        return res