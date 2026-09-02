class Solution:

    # using DFS


    # def dfs(self, i, j, new_color, initial_color, visited, r, c):
    #         # base conditions
    #         if i<0 or i>=r or j<0 or j>=c:
    #             return
    #         if visited[i][j]!=initial_color:
    #             return
    #         if visited[i][j]==new_color:
    #             return
    #         visited[i][j]=new_color
    #         self.dfs(i+1, j, new_color, initial_color, visited, r, c ) #down
    #         self.dfs(i, j-1, new_color, initial_color, visited, r, c) #left
    #         self.dfs(i-1, j, new_color, initial_color, visited, r, c) #up
    #         self.dfs(i, j+1, new_color, initial_color, visited, r, c) #right
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if image[sr][sc]==color:
        #     return image
        # visited=deepcopy(image)
        # r, c=len(visited), len(visited[0])
        # initial_color=visited[sr][sc]
        # self.dfs(sr, sc, color, initial_color, visited, r, c)
        # return visited

   
   
#    using BFs
   
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: 
        if image[sr][sc]==color:
            return image
        visited=deepcopy(image)    
        r, c=len(visited), len(visited[0])
        initial_color=visited[sr][sc]
        queue=deque()
        queue.append((sr, sc))
        while len(queue)!=0:
            i, j=queue.popleft()
            visited[i][j]=color
            for x,y in [(-1,0),(0, -1), (1, 0), (0,1)]:
                new_i=i+x
                new_j=j+y
                if new_i<0 or new_i>=r or new_j<0 or new_j>=c:
                    continue
                if visited[new_i][new_j]!=initial_color:
                    continue
                queue.append((new_i, new_j))
        return visited