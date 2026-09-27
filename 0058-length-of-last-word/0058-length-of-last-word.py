class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        last=len(s)-1
        while last>=0 and s[last]==' ':
            last-=1
        while last>=0 and s[last]!=' ':
            l+=1
            last-=1
        return l    