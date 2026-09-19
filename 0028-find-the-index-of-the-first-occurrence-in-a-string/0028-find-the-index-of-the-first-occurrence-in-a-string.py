class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        for i in range(len(haystack)):
            window=haystack[i:i+k]
            if window==needle:
                return i
        return -1        
