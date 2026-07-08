class Solution:
    def fun(self, n):
        tot=0
        while n>0:
            d=n%10 #9
            n//=10 #1
            tot+=d*d
        return tot    
    def isHappy(self, n):
        slow=n
        fast=n
        while True:
            slow=self.fun(slow)
            fast=self.fun(fast)
            fast=self.fun(fast)
            if fast ==1:
                return True
            if slow==fast :
                return False
s=Solution()
print(s.isHappy(19))      