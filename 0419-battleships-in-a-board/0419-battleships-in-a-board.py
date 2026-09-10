class Solution:
    def dfs(self, r, c, visited, board, rows, cols):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if visited[r][c]==1 or board[r][c]==".":
            return 
        visited[r][c]=1
        self.dfs(r+1, c, visited, board, rows, cols)
        self.dfs(r-1, c, visited, board, rows, cols)
        self.dfs(r, c+1, visited, board, rows, cols)
        self.dfs(r, c-1, visited, board, rows, cols)
            
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols=len(board), len(board[0])
        count=0
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="X" and not visited[r][c]:
                    self.dfs(r,c, visited, board, rows, cols)
                    count+=1
        return count        