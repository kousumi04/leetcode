class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int: 
        grid_copy=deepcopy(grid)
        rows=len(grid_copy)
        cols=len(grid_copy[0])
        perimeter=0
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c]==1:
                    queue.append((r,c))
                    grid_copy[r][c]=2
                    break
            if queue:
                break        
        while len(queue)!=0:
            i,j=queue.popleft()
            for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj=i+x, j+y
                if ni<0 or ni>=rows or nj<0 or nj>=cols:
                    perimeter+=1
                else:    
                    if grid_copy[ni][nj]==0:
                        perimeter+=1
                    elif grid_copy[ni][nj]==1:
                        queue.append((ni, nj))
                        grid_copy[ni][nj]=2  
        return perimeter        