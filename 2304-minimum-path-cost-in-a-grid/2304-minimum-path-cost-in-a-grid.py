class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1, m):
            for j in range(n):
                temp = [0]*n
                for k in range(n):
                    temp[k] = grid[i][j] + moveCost[grid[i-1][k]][j] + dp[i-1][k]
                dp[i][j] = min(temp)
        return min(dp[-1])