"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
				[0,0,0,0,0,0,0,1,1,1,0,0,0],
				[0,1,1,0,1,0,0,0,0,0,0,0,0],
				[0,1,0,0,1,1,0,0,1,0,1,0,0],
				[0,1,0,0,1,1,0,0,1,1,1,0,0],
				[0,0,0,0,0,0,0,0,0,0,1,0,0],
				[0,0,0,0,0,0,0,1,1,1,0,0,0],
				[0,0,0,0,0,0,0,1,1,0,0,0,0]]

Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]

Output: 0
"""

# Using DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen=set()
        def getArea(r,c):
            if not (0<=r<len(grid) and 0<=c<len(grid[0]) and (r,c) not in seen and grid[r][c]):
                return 0
            seen.add((r,c))
            return (1+getArea(r+1,c)+getArea(r-1,c)+getArea(r,c-1)+getArea(r,c+1))
        return max(getArea(r,c) for r in range(len(grid)) for c in range(len(grid[0])))
                
