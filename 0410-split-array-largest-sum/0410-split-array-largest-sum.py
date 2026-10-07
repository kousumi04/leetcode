class Solution:
    def splitArray(self, nums: list[int], k:int) -> int:
        def canSplit(limit):
            count=1
            curSum=0
            for n in nums:
                if curSum+n>limit:
                    count+=1
                    curSum=n
                else:
                    curSum+=n    
            return count<=k     
        l=max(nums)
        r=sum(nums)
        while l<r:
            mid=(l+r)//2
            if canSplit(mid):
                r=mid
            else:
                l=mid+1
        return r