class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freq={}
        for ch in t:
            freq[ch]=freq.get(ch, 0)+1
        count=len(t)
        left=0
        minLen=float("inf")
        start=0
        for right in range(len(s)):
            if s[right] in freq:
                if freq[s[right]] > 0:
                    count-=1
                freq[s[right]]-=1
            while count==0:
                if right-left+1<minLen:
                    minLen=right-left+1
                    start=left
                if s[left] in freq:
                    freq[s[left]] += 1

                    if freq[s[left]] > 0:
                        count += 1
                left += 1
        if minLen == float('inf'):
            return ""
        return s[start:start + minLen]
