class Solution:
    def addMinimum(self, word: str) -> int:
        ans=0
        prev='c'
        for ch in word:
            if prev=='a' and ch=='c':
                ans+=1
            elif prev=='b' and ch=='a':
                ans+=1
            elif prev=='c' and ch=='b':
                ans+=1
            elif prev==ch:
                ans+=2
            prev=ch
        
        if prev=='a':
            ans+=2
        elif prev=='b':
            ans+=1
        return ans        


        