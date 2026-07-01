class Solution:
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        countP, countS={}, {}
        for i in range(len(p)):
            countP[p[i]]=countP.get(p[i],0)+1
            countS[s[i]]=countS.get(s[i],0)+1
        res=[0] if countS==countP else []
        l=0
        for r in range(len(p), len(s)):
            countS[s[r]]=countS.get(s[r],0)+1
            countS[s[l]]-=1

            if countS[s[l]]==0:
                countS.pop(s[l])
            l+=1
            if countS==countP:
                res.append(l)   
        return res        
sol=Solution()
s="cbaebabacd"
p="abc"
print(sol.findAnagrams(s,p))


