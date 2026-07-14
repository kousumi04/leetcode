# class Solution:
#     def characterReplacement(self, s, k):
#         count={}
#         res=0
#         left=0

#         for right in range(len(s)):
#             count[s[right]]=count.get(s[right],0)+1
            
#             while (right-left+1)-max(count.values())>k:
#                 count[s[left]]-=1
#                 l+=1
#             res=max(res, right-left+1)
#         return res    

# sol=Solution()
# s="ABAB"
# k=4
# print(sol.characterReplacement(s,k))   



# mII-

class Solution:
    def characterReplacement(self, s, k):
        left=0
        res=0
        maxf=0        
        count={}
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxf=max(maxf, count[s[right]])
            while (right-left+1)-maxf>k:
                count[s[left]]-=1
                left+=1
            res=max(res, right-left+1)
        return res

sol=Solution()
s="ABAB"
k=4
print(sol.characterReplacement(s,k))  
