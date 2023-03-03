from typing import List
class Solution:
    def generateMatrix(self, n:int) -> List[List[int]]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        matrix = [[0]*n for i in range(n)]
        row, col, dirInx = 0, 0, 0
        for i in range(n*n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirInx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirInx = (dirInx + 1) % 4
                dx, dy = dirs[dirInx]
            row, col = row + dx, col + dy

        return matrix

case1 = Solution()
print(case1.generateMatrix(3))