class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2, 3]
        dp += [0]*(n+1)
        
        if n <= 3:
            return n
        
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
            