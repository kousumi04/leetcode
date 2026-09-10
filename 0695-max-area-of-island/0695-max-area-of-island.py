class Solution:
    def dfs(self, r,c, visited, grid, rows, cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return 0
        if visited[r][c]==1 or grid[r][c]==0:
            return 0
        visited[r][c]=1
        area=1
        area+=self.dfs(r+1, c, visited, grid, rows, cols)
        area+=self.dfs(r-1, c, visited, grid, rows, cols)
        area+=self.dfs(r, c+1, visited, grid, rows, cols)
        area+=self.dfs(r, c-1, visited, grid, rows, cols)    
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        rows, cols=len(grid), len(grid[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    area=self.dfs(r,c, visited, grid, rows, cols)
                    count=max(count, area)
        return count