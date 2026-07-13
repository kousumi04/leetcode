class Solution:
    # # BRUTE FORCE WON'T WORK HERE
    # def maxArea(self, height):
    #     res=0
    #     for i in range(len(height)):
    #         for j in range(i+1, len(height)):
    #             area=(i-j)*min(height[i], height[j])
    #             res=max(res, area)
    #     return res  


    def maxArea(self, height):
        left=0
        right=len(height)-1
        res=0
        while left<right:
            area=(right-left)* min(height[left], height[right])
            res=max(res, area)
            if height[left]<height[right]:
                left+=1
            # elif height[left]>height[right]:
            #     right-=1
            else:
                right-=1   
        return res         
s=Solution()
height=[1,8,6,2,5,4,8,3,7]    
print(s.maxArea(height))  