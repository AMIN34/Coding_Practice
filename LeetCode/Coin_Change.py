"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

# Solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).

        #The time complexity is O(amount * coins.length) and the space complexity is O(amount)
        dp= [0]+ [float('inf')]*amount;
        for i in range(1+amount):
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return -1 if dp[-1]==float('inf') else dp[-1]
    #checking the last element of dp, i.e. actual problem whether its modified or not
    # if it is, then okay other wise cannot and return -1
