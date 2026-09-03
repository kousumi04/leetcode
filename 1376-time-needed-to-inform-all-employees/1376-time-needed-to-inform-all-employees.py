from collections import defaultdict
class Solution:
    def dfs(self,manager, informTime, adjList):
        maxTime=0
        for node in adjList[manager]:
            maxTime=max(maxTime, self.dfs(node,informTime, adjList))
        return maxTime+informTime[manager]    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n<=0:
            return 0
        adjList=[[] for _ in range(n)]
        for i in range(n):
            if manager[i]!=-1:
                adjList[manager[i]].append(i)
        return self.dfs(headID, informTime, adjList)