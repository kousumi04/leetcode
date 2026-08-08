class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s) 
        t=list(t)
        s.sort()
        t.sort()
        # freq1={}
        # freq2={}
        # for key1 in s:
        #     if key1 in freq1.keys():
        #         freq1[key1]+=1
        #     else:
        #         freq1[key1]=1
        # for key2 in t:
        #     if key2 in freq2.keys():
        #         freq2[key2]+=1
        #     else:
        #         freq2[key2]=1
        if s==t:
            return True
        else:
            return False


            