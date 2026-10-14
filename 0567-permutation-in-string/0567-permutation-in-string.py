class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2=len(s1), len(s2)
        while n1>n2:
            return False
        
        s1_counts=[0]*26
        s2_counts=[0]*26
        for i in range(n1):
            # in this case 0, 1, 2
            s1_counts[ord(s1[i])-ord('a')]+=1
            # ord(s1[i]) --> ASCII value of the character
            s2_counts[ord(s2[i])-ord('a')]+=1
        if s1_counts==s2_counts:
            return True
        for i in range(n1, n2):
            # in this case (3,8)
            s2_counts[ord(s2[i])-ord('a')]+=1 #add acharacter
            s2_counts[ord(s2[i-n1])-ord('a')]-=1
            if s1_counts==s2_counts:
                return True
        return False 