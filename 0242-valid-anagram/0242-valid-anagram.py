class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)>len(t):
        #     return []
        countS =Counter(s)
        for char in t:
            if char not in countS:
                return False
            countS[char]-=1
            if countS[char]==0:
                del countS[char]    
        return len(countS)==0    
