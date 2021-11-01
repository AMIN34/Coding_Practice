"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

# Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r,c = len(board),len(board[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1)]  # Movements
        
        def dfs(x:int,y:int)-> None:
            if 0<= x < r and 0<= y < c and board[x][y]=='O':
                board[x][y]="#" # marked
                for dx,dy in direction:
                    dfs(x+dx,y+dy)
                
        # For the edges
        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for i in range(1,c-1):
            dfs(0,i)
            dfs(r-1,i)
        
        # Concurring surronded 'O'
        for i,j in itertools.product(range(r),range(c)):
            board[i][j]='X' if board[i][j]!='#' else 'O'
