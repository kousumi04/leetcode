class Solution:
    def maximumSum(self, arr):
        i=0
        nodel = onedel=res=arr[i]
        for i in arr[1:]:
            if nodel<0:
                nodel=0
            if i>=0:
                nodel+=i
            else:
                nodel=max(nodel+i, onedel)    
            if onedel<0:
                onedel=0
            onedel+=i
            res=max(res, max(nodel, onedel))       
        return res    

s=Solution()
arr =[1,-2,0,3]
print(s.maximumSum(arr))