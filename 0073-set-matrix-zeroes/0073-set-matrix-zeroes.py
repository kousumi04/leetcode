class Solution:
    # def markInf(self, matrix, row, col):
    #     r, c=len(matrix), len(matrix[0])
    #     for i in range(0, r):
    #         if matrix[i][col]!=0:
    #             matrix[i][col]=float("inf")
    #     for j in range(0, c):
    #         if matrix[row][j]!=0:
    #             matrix[row][j]=float("inf")

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols=len(matrix), len(matrix[0])
        rTrack=[0 for _ in range(rows)]
        cTrack=[0 for _ in range(cols)]
        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j]==0:
                    rTrack[i]=-1
                    cTrack[j]=-1

        for i in range(0, rows):
            for j in range(0, cols):
                if rTrack[i]==-1 or cTrack[j]==-1:
                    matrix[i][j]=0
                    
        

         