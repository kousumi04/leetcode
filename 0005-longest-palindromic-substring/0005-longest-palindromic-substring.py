class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            odd=expand(s, i, i)
            even=expand(s, i, i+1)
            if len(odd)>len(ans):
                ans=odd
            if len(even)>len(ans):
                ans=even
        return ans

def expand(s, i, j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]