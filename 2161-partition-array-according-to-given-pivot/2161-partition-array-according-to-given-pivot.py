class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        neg, pos=[], []
        p=[]
        size=len(nums)
        for i in nums:
            if i<pivot:
                neg.append(i)
            if i>pivot:
                pos.append(i)
            if i==pivot:
                p.append(i)
        return neg+p+pos         