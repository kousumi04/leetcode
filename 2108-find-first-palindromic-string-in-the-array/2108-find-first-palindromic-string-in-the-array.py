class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        ch=0
        
        def palindrome(s):
            return s==s[::-1]

        for ch in words:
            if palindrome(ch):
                return ch
                break
        return ""        
