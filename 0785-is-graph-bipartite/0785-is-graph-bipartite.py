class Solution:
    def dfs(self, currNode, visited, graph, color):
        visited[currNode]=color
        for adjNode in graph[currNode]:
            if visited[adjNode]!=-1:
                if visited[adjNode]==color:
                    return False
            else:
                # if color==0:
                #     ans=self.dfs(adjNode, visited, graph, 1) 
                # else:
                #     ans=self.dfs(adjNode, visited, graph, 0)
                ans=self.dfs(adjNode, visited, graph, 1-color) 
                if ans==False:
                    return False
        return True                       
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes=len(graph)
        visited=[-1]* nodes
        for i in range(0, nodes):
            if visited[i]==-1:
                res=self.dfs(i,visited, graph,0)
                if res==False:
                    return False
        return True            