class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recursion(row, col):
            if col == 0 and row == 0:
                return 1
            if row < 0 or col < 0:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            
            up = recursion(row-1, col)
            left = recursion(row, col-1)
            
            dp[row][col] = up + left
            return dp[row][col]
        
        dp = [[-1]*n for _ in range(m)]
        return recursion(m-1, n-1)