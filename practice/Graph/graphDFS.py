def dfs(node, res, visited, adj):
    visited[node]=1
    res.append(node)
    for n in adj[node]:
        if visited[n]==0:
            dfs(n, res, visited, adj)


numberOfNodes=8
adj_list=[[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]    
visited=[0]*(numberOfNodes+1)
res=[]
dfs(1, res, visited, adj_list)
print(res)