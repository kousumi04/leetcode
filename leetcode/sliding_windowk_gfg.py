class Solution:
    def longestKSubstr(self, s, k):
        n=len(s)
        low=0
        freq={}
        res=-1
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            '''This line updates the frequency count of the 
            character s[right] in the dictionary freq.
            s[right] → current character.
            freq.get(s[right], 0) → gets the current count of that character.
            If the character exists in freq, it returns its count.
            If it does not exist, it returns 0.
            + 1 → increases the count by 1.
            The result is stored back in freq[s[right]].'''
            
            while len(freq)>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    freq.pop(s[low])
                low+=1
            if len(freq)==k:
                l=high-low+1
                res=max(l, res)
        return res                 
sol=Solution()
s = "aabacbebebe" 
k = 3
print(sol.longestKSubstr(s,k))