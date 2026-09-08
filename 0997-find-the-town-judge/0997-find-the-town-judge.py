class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by=[0]*(n+1)
        trusts=[0]*(n+1)
        for p1, p2 in trust:
            trusted_by[p2]+=1
            trusts[p1]+=1
        for i in range(1, n+1):
            if trusted_by[i]==n-1 and trusts[i]==0:
                return i
        return -1        