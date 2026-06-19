class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        res=arr[0]+arr[1]+arr[2]
        # positive infinity
        ans=0
        maxDiff=float('inf')
        for i in range(0, len(arr)-2):
            left=i+1 
            right=len(arr)-1 #last element
            while left<right:
                s=arr[i]+arr[left]+arr[right] #-2+0+3=1 ->1st iteration

                '''if s>=sum decrement right.
                incrementing left will always give sum>sum''' 
                if s>=sum: #1>=2, false
                    right-=1
                else:
                    '''if s<sum then ans=0+(3-0) -> 3'''
                    ans=ans+(right-left)
                    left+=1
        return ans

s=Solution()
arr=[-2, 0, 1, 3]
sum=2
print(s.countTriplets(sum, arr))        