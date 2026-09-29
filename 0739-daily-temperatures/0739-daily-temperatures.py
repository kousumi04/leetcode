class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        days=[0]*(len(temperatures))
        t=temperatures
        for i in range(len(temperatures)):
            while len(stack)!=0 and temperatures[i]> temperatures[stack[-1]]:
                j=stack.pop()
                days[j]=i-j
            stack.append(i)
        return days        