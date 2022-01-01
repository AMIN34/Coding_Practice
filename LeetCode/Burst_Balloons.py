"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
"""

# Solution
"""
Let us consider dp[i][j] the maximum number of coins we can get, popping balls from i to j, not including i and j. Why it is enough to keep these values? Let us look at the last popped balloon with number k. Then our balloons are separated into two groups: to the left of this balloon and the the right and we can write:

	dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) for k in (i+1,j),

where k is the index of the last balloon burst in (i, j).
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = [1] + nums + [1]
        n=len(nums)+2
        dp=[[0]*n for _ in range(n)]
        
        for i in range(n-2,-1,-1):
            for j in range(i+2,n):
                dp[i][j]=max(N[i]*N[k]*N[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        return dp[0][n-1]
