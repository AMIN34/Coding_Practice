"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

# Method 1)
class Solution:
    #For checking Fresh Oranges
    def isValid(self, li, r, c, n, m):
        if 0<=r<n and 0<=c<m and li[r][c] == 1: #if fresh return
            return True
        return False
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: #rotten orange
                    queue.append((0, i, j))
        row,col = [0, -1, 0, 1], [-1, 0,  1, 0]
        last_time = 0
        while len(queue):
            for _ in range(len(queue)): #going level wise
                time, i, j = queue.popleft()
                last_time = time
                for k in range(4):
                    nr, nc = i+row[k], j+col[k]
                    if self.isValid(grid, nr, nc, n, m): #check neighbors for fresh orange
                        grid[nr][nc] = 2 
                        queue.append((time+1, nr, nc))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: #According to question
                    return -1
        return last_time
        
