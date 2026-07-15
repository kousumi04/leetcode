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
        res=0
        left=0
        maxf=0
        c={}
        for right in range(len(s)): 
            # stores the count of each character
            c[s[right]]=c.get(s[right],0)+1
            # stores the max of the count of the characters
            maxf=max(maxf, c[s[right]])
            # cond for checking window size-max freq is >k the decrement count from the left 
            while (right-left+1)-maxf>k:
                c[s[left]]-=1
                # increment left
                left+=1
            res=max(res, right-left+1)    
        return res    

sol=Solution()
s="ABAB"
k=4
print(sol.characterReplacement(s,k))  
