class Solution:
    def maxSlidingWindow(self, nums, k):
        # res=[]
        # maxf=0
        # brute force
        # for i in range( len(nums)-k):
        #     maxf=nums[i]
        #     for j in range(i, i+k-1):
        #         maxf=max(maxf, nums[j])
        #     res.append(maxf)
        # return res

        import collections
        # m2
        res=[]
        q=collections.deque()
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            while q and q[0]<l:
                q.popleft()

            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res    

s=Solution()
nums=[1, 3, -1, -3, 5, 3, 6, 7]
k=3
print(s.maxSlidingWindow(nums,k))           