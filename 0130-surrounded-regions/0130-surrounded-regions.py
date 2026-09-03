class Solution:
    def  dfs(self, r, c,visited, rows, cols, board):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if board[r][c]=="X":
            return 
        if visited[r][c]==1:
            return        
        visited[r][c]=1
        self.dfs(r-1,c,visited, rows, cols, board) #up
        self.dfs(r,c-1,visited, rows, cols, board) #left
        self.dfs(r,c+1,visited, rows, cols, board) #right
        self.dfs(r+1,c,visited, rows, cols, board) #down
    def solve(self, board: List[List[str]]) -> None:
        rows, cols=len(board), len(board[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        # upper row
        r=0
        c=0,0
        for c in range(cols):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows, cols, board)
        # last row
        r=rows-1
        c=0,0
        for c in range(cols):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows, cols, board)
        # first col
        r=0
        c=0
        for r in range(rows):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows, cols, board)
        # last col
        r=0
        c=cols-1
        for r in range(rows):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows, cols, board)            

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and visited[r][c]==0:
                    board[r][c]="X"