class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v=len(graph)
        adjList=[[] for _ in range(v)]
        for node in range(0, v):
            for adjNode in graph[node]:
                adjList[adjNode].append(node)

        queue=deque()

        # calc indegrees
        indegrees=[0 for _ in range(v)]
        for node in range(v):
            indegrees[node] = len(graph[node])

        # add all the node with indegrees o in the queue 
        for node in range(0,v):
            if indegrees[node]==0:
                queue.append(node)
        res=[]

        while len(queue)!=0:
            node=queue.popleft()
            res.append(node)
            for adjNode in adjList[node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode]==0:
                    queue.append(adjNode)
        res.sort()
        return res