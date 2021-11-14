"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

Question was also in GFG ( I guess )
"""

# Solution
# using Closure number / Catalan number
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        res = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    res.append('({}){}'.format(left,right))
        return res
