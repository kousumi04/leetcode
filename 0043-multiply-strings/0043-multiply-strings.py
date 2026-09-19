class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                n1=ord(num1[i])-ord('0')
                n2=ord(num2[j])-ord('0')
                res[i+j+1]+=n1*n2
        for i in range(len(res)-1, 0, -1):
            carry=res[i]//10
            res[i]%=10
            res[i-1]+=carry
        ans = ""
        for digit in res:
            ans += str(digit)
        i = 0
        while i < len(ans)-1 and ans[i] == '0':
            i += 1

        return ans[i:]