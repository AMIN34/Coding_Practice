"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
"""

# Solution
class Solution:
    def integerBreak(self, n: int) -> int:
        # create a table, infer from it, that it have a pattern in it's solution
        c = [0,0,1,2,4,6,9] #solutions for n<=6
        if n<7:
            return c[n]
        dp = c + [0]*(n-6) # dp for the rest of the solution
        for i in range(7,n+1):
            dp[i] = 3*dp[i-3] # from the pattern
        return dp[-1] # the last element is the required answer
