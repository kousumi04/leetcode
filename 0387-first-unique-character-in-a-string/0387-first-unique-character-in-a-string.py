class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for char in range(len(s)):
            count[s[char]]=count.get(s[char],0)+1
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1 
            