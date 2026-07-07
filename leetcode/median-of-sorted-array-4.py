class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if n==1:
            return float(nums1[0])
        if n%2!=0:
            return float(nums1[n//2])
        else:
            m1=n//2-1
            m2=n//2
            return (nums1[m1]+nums1[m2])/2
s=Solution()        
nums1=[1,3]
nums2=[2,4]
print(s.findMedianSortedArrays(nums1, nums2))
