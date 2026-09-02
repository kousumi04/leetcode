from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows, cols = len(mat), len(mat[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        dist = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()

        # Put all 0s into the queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = 1

        while len(queue) != 0:

            i, j, d = queue.popleft()

            dist[i][j] = d

            for x, y in [(1, 0), (0, -1), (0, 1), (-1, 0)]:

                new_i = i + x
                new_j = j + y

                # Boundary check
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if visited[new_i][new_j] == 1:
                    continue

                queue.append((new_i, new_j, d + 1))
                visited[new_i][new_j] = 1

        return dist