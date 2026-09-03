class Solution:
       
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[0 for _ in range(len(rooms))]
        def dfs( room):
            if room<0:
                return
            visited[room]=1
            for key in rooms[room]:
                if visited[key]==0:
                    dfs(key) 
        dfs(0)
        return sum(visited)==len(rooms)            
