class Solution:
    def dfs(self, r, c, visited, grid, rows, cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return 
        if grid[r][c]==0:
            return    
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs(r+1, c, visited, grid, rows, cols)    
        self.dfs(r-1, c, visited, grid, rows, cols)    
        self.dfs(r, c+1, visited, grid, rows, cols)    
        self.dfs(r, c-1, visited, grid, rows, cols)    

    def numEnclaves(self, grid: List[List[int]]) -> int:
        count=0
        rows, cols=len(grid), len(grid[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]           

        # upper row
        r=0
        c=0,0
        for c in range(cols):
            if grid[r][c]==1:
                if visited[r][c]==0:
                    self.dfs(r, c, visited, grid, rows, cols)

        # last row
        r=rows-1
        c=0,0
        for c in range(cols):
            if grid[r][c]==1:
                if visited[r][c]==0:
                    self.dfs(r, c, visited, grid, rows, cols)

        #first col
        r=0
        c=0
        for r in range(rows):
            if grid[r][c]==1:
                if visited[r][c]==0:
                    self.dfs(r, c, visited, grid, rows, cols)

        #last col
        r=0
        c=cols-1
        for r in range(rows):
            if grid[r][c]==1:
                if visited[r][c]==0:
                    self.dfs(r, c, visited, grid, rows, cols)   
                             
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    count+=1
        return count            