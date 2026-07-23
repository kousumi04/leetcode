class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=[]
        for char in operations:
            if char=="+":
                total=ops[-1]+ops[-2]
                ops.append(total)
            elif char=="D":
                ops.append(ops[-1]*2)
            elif char=="C":
                ops.pop()
            else:
                ops.append(int(char))
        return sum(ops)


                

