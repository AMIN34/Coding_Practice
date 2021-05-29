class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 1 
        
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
            
        return dp[-1]