class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n=len(image), len(image[0])
        cur_color=image[sr][sc]
        if cur_color==color:
            return image
        cur=[[sr, sc]]    
        image[sr][sc]=color
        while cur:
            new_layer=[]
            for r,c in cur:
                check=[(r+1,c),(r-1,c), (r,c+1), (r, c-1)]
                for cr, cc in check:
                    if cr>=0 and cc>=0 and cr<m and cc<n and image[cr][cc]==cur_color:
                        image[cr][cc]=color
                        new_layer.append((cr, cc))
            cur=new_layer           
        return image     