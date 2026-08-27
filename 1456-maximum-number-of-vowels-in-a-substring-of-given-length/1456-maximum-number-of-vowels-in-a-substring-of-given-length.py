class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr=0
        for i in range(k):
            if s[i] in "aeiou":
                curr+=1
        max_vowels=curr        
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                curr+=1
            if s[i-k] in "aeiou":
                curr-=1
            max_vowels=max(max_vowels, curr)
        return max_vowels    
             
        