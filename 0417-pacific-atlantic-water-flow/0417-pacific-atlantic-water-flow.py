class Solution:
    def dfs(self, r,c, visited, heights, rows, cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return 
        if visited[r][c]:
            return 
        visited[r][c]=True   
        if r+1<rows and heights[r+1][c]>=heights[r][c]:
            self.dfs(r+1,c, visited, heights, rows, cols)

        if r-1>=0 and heights[r-1][c]>=heights[r][c]:    
            self.dfs(r-1,c, visited, heights, rows, cols) 
        
        if c+1<cols and heights[r][c+1]>=heights[r][c]:    
            self.dfs(r,c+1, visited, heights, rows, cols) 
        
        if c-1>=0 and heights[r][c-1]>=heights[r][c]:    
            self.dfs(r,c-1, visited, heights, rows, cols)    

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols=len(heights), len(heights[0])
        atlantic=[[False] *cols for _ in range(rows)]
        pacific=[[False] *cols for _ in range(rows)]
        for c in range(cols):
            self.dfs(0,c, pacific, heights, rows, cols)
        for r in range(rows):    
            self.dfs(r,0, pacific, heights, rows, cols)
        for c in range(cols):
            self.dfs(rows-1,c, atlantic, heights, rows, cols)
        for r in range(rows):    
            self.dfs(r,cols-1, atlantic, heights, rows, cols) 
        res=[]    
        for r in range(rows):
            for c in range(cols):       
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])  
        return res        
                