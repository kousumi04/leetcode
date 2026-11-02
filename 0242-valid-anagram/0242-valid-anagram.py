class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # s=list(s) 
        # t=list(t)
        # s.sort()
        # t.sort() 
        # if s==t:
        #     return True
        # else:
        #     return False 



        # return (sorted(s)==sorted(t))


        freq={}
        if len(s)!=len(t):
            return False
        else:    
            for ch in s:
                if ch not in freq:
                    freq[ch]=0
                freq[ch]+=1   
            for ch in t:
                if ch not in freq:
                    return False
                    break
                freq[ch]-=1

                if freq[ch]<0:
                    return False
                    break
            else:
                return all(value == 0 for value in freq.values())

