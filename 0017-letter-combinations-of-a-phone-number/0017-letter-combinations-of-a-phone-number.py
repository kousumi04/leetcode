class Solution:
    def solve(self, i, subset, phoneMap, digs, res):
        if i>=len(digs):
            res.append("".join(subset))
            return 

        for ch in phoneMap[digs[i]]:
            subset.append(ch)
            self.solve(i+1, subset, phoneMap, digs, res)
            subset.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        res=[]
        phoneMap={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        self.solve(0, [], phoneMap, digits, res)
        return res