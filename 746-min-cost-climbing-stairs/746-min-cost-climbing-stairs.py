class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """cost.append(0)
        def recursion(n):
            if dp[n] != 0:
                return dp[n]
            if n == 0 or n == 1:
                return cost[n]
            
            jump = recursion(n-1)
            doubleJump = float('inf')
            if n > 1:
                doubleJump = recursion(n-2)
            dp[n] = cost[n] + min(jump, doubleJump)
            return dp[n]
        dp = [0]*(len(cost) + 1)
        return recursion(len(cost)-1)"""
        
        cost.append(0)
        dp = [0]*(len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return dp[len(cost)-1]