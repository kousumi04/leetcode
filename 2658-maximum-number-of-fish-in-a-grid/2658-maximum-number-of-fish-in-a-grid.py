class Solution:
    def dfs(self, r, c, visited, grid, rows, cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return 0
        if visited[r][c]==1 or grid[r][c]==0:
            return 0
        visited[r][c]=1
        fish=grid[r][c]
        fish+=self.dfs( r+1, c, visited, grid, rows, cols)
        fish+=self.dfs( r-1, c, visited, grid, rows, cols)
        fish+=self.dfs( r, c+1, visited, grid, rows, cols)
        fish+=self.dfs( r, c-1, visited, grid, rows, cols)
        return fish        
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        maxFish=0
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                fish=self.dfs(r, c, visited, grid, rows, cols)
                maxFish=max(maxFish, fish)
        return maxFish        