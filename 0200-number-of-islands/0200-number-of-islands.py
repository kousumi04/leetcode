class Solution:
    def dfs(self, r, c, visited, grid, rows, cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if visited[r][c]==1 or grid[r][c]=="0":    
            return
        visited[r][c]=1
        self.dfs(r-1, c,visited, grid, rows, cols) 
        self.dfs(r+1, c,visited, grid, rows, cols) 
        self.dfs(r, c-1,visited, grid, rows, cols) 
        self.dfs(r, c+1,visited, grid, rows, cols) 
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols=len(grid), len(grid[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]==0:
                    self.dfs(r, c,visited,grid,rows, cols)
                    count+=1
        return count   