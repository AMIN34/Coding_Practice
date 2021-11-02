"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)


Example 2:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""

# Solution
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r,c= len(grid),len(grid[0])
        start,count = None, 0
        for i in range(r):
            for j in range(c):
                count += grid[i][j] == 0
                if not start and grid[i][j]==1:
                    start = (i,j)
        
        def backtrack(i:int, j:int)-> int:
            nonlocal count # accessing count variable
            res = 0 # no. of ways
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)): # all possible moevments
                if 0 <= x < r and 0<= y < c: # border check
                    if grid[x][y]==0:
                        # okay to traverse
                        grid[x][y] = -1 # traversed
                        count -=1
                        res += backtrack(x,y)
                        # backtrack and reset
                        grid[x][y]=0
                        count += 1
                    elif grid[x][y]==2:
                        res += count==0 # every path have been traversed
            return res
        return backtrack(start[0],start[1])
                        
