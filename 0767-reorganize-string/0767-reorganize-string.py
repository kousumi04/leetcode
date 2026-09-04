class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        res=[]
        prev=""
        for _ in range(len(s)):
            best=None
            for ch in count:
                if ch!=prev and count[ch]>0:
                    if best is None or count[ch]>count[best]:
                        best=ch
            if best is None:
                return ""

            res.append(best)
            count[best]-=1
            prev=best
        return "".join(res)                    
