class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
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
        return recursion(len(cost)-1)