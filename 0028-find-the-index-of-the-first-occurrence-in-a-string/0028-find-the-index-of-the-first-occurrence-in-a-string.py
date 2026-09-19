class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        h=len(haystack)
        for i in range(h-k+1):
            window=haystack[i:i+k]
            if window==needle:
                return i
        return -1        
