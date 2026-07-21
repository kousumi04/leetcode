class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nge={}
        for i in nums2:
            while stack and i>stack[-1]:
                smaller=stack.pop()
                nge[smaller]=i
            stack.append(i)
        while stack:
            nge[stack.pop()]=-1
        ans=[]
        for i in nums1:
            ans.append(nge[i])
        return ans      
