n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
src, dest = map(int, input().split())
dist = [999999] * (n + 1)
parent = [-1] * (n + 1)
visited = [False] * (n + 1)
dist[src] = 0
for _ in range(n):
    u = -1
    for i in range(1, n + 1):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
    visited[u] = True
    for v in range(1, n + 1):
        if graph[u][v] != 0:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
path = []
x = dest
while x != -1:
    path.append(x)
    x = parent[x]
path.reverse()
print(*path)
print(dist[dest])