class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        indegrees=[0 for _ in range(numCourses)]
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegrees[v]+=1
        queue=deque()    
        res=[]
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            cur=queue.popleft()
            res.append(cur)
            for adjNode in adj_list[cur]:
                indegrees[adjNode]-=1
                if indegrees[adjNode]==0:
                    queue.append(adjNode)
        if len(res)==numCourses:
            return True
        return False               
