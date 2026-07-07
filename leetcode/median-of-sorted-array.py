class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        return nums1
s=Solution()        
nums1=[1,3]
nums2=[2]
print(s.findMedianSortedArrays(nums1, nums2))
