"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

# Method 1)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        r,c = len(mat),len(mat[0])
        dist_mat =[[math.inf]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    dist_mat[i][j]=0
                else:
                    if i>0:
                        dist_mat[i][j]=min(dist_mat[i][j],dist_mat[i-1][j]+1)
                    if j>0:
                        dist_mat[i][j]=min(dist_mat[i][j],dist_mat[i][j-1]+1)
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if mat[i][j]==0:
                    dist_mat[i][j]=0
                else:
                    if i+1<r:
                        dist_mat[i][j]=min(dist_mat[i][j],dist_mat[i+1][j]+1)
                    if j+1<c:
                        dist_mat[i][j]=min(dist_mat[i][j],dist_mat[i][j+1]+1)
        return dist_mat
        
