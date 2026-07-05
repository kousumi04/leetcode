class Solution:
    def merge(self, nums1, m, nums2, n):
        res=[]
        i, j=0, 0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
            else:  
                res.append(nums2[j])  
                j+=1
        res=res+nums1[i:m]
        res=res+nums2[j:n]
        nums1[:]=res
        return nums1
s=Solution()        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3       
print(s.merge(nums1, m, nums2, n))
