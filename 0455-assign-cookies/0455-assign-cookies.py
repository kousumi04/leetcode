class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        g.sort()
        s.sort()
        m, n=len(g), len(s)
        left, right=0,0
        while left<m and right<n:
            if g[left]<=s[right]:
                count+=1
                left+=1
            right+=1
        return count    



