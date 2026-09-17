class Solution:
    def solve(self, i, total, brackets, res):
        if i>=len(brackets):
            if total==0:
                res.append("".join(brackets))
            return 
        if total>len(brackets)//2:
            return
        elif total<0:
            return
        brackets[i]="("
        s=total+1 
        self.solve(i+1,s, brackets, res)               
        brackets[i]=")"
        s=total-1 
        self.solve(i+1,s, brackets, res) 

    def generateParenthesis(self, n: int) -> list[str]:
        brackets=[""] * (n*2)
        res=[]
        self.solve(0,0,brackets, res)
        return res                  