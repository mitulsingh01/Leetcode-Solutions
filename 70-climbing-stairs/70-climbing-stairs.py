class Solution:
    def climbStairs(self, n: int) -> int:
        #recursion
        """if n == 0 or n == 1:
            return 1
        
        left = self.climbStairs(n-1)
        right = self.climbStairs(n-2)
        
        return left + right"""
        #memoization
        """dp = [-1]*(n+1)
        
        def recursion(n, dp):
            if n == 1 or n == 2:
                return n
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = recursion(n-1, dp) + recursion(n-2, dp)
            
            return dp[n]
        
        
        return recursion(n, dp)"""
        #tabulation
        """dp = [-1]*(n+1)
        
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]"""
        #space optimization
        if n == 1 or n == 2:
                return n
        
        prev2, prev = 1, 2
        for i in range(2, n):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        
        return prev
        
            