class Solution:
    def dfs(self, i, j, new_color, initial_color, visited, r, c, border, grid):
        if i<0 or i>=r or j<0 or j>=c:
            return 
        if visited[i][j] or grid[i][j]!=initial_color:
            return
        visited[i][j]=True
        if (i==0 or i==r-1 or j==0 or j==c-1 or 
            grid[i+1][j]!=initial_color or grid[i-1][j]!=initial_color or 
            grid[i][j+1]!=initial_color or grid[i][j-1]!=initial_color):
            border.append((i,j))
        self.dfs(i+1, j, new_color, initial_color, visited, r, c, border, grid)
        self.dfs(i-1, j, new_color, initial_color, visited, r, c, border, grid)
        self.dfs(i, j+1, new_color, initial_color, visited, r, c, border, grid)
        self.dfs(i, j-1, new_color, initial_color, visited, r, c, border, grid)

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        if grid[row][col]==color:
            return grid
        initial_color=grid[row][col]    
        r,c=len(grid), len(grid[0])    
        visited=[[False] *c for _ in range(r)]
        border=[]
        self.dfs(row,col, color, initial_color, visited, r, c, border, grid)
        for i, j in border:
            grid[i][j]=color
        return grid
