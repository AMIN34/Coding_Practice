"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
"""

# Solution
from math import factorial as f
class Solution:
    def numTrees(self, n: int) -> int:
        """
        Use Catalan Number. Good for finding no. of different forms
        """
        return f(2*n)//(f(n+1)*f(n))
