class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """def recursion(row, col):
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
        return recursion(m-1, n-1)"""
        
        """dp = [[-1]*n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]"""
        
        """prev = [0]*n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                else:
                    curr[j] = prev[j] + curr[j-1]
            prev = curr
        return prev[n-1]"""
        
        N = m + n - 2
        r = m - 1
        res = 1
        for i in range(1, r+1):
            res *= ((N - r + i)/i)
        if(res > int(res)+0.5):
            return math.ceil(res)
        return int(res)