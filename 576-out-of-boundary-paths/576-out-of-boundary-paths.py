class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 1000000007
        def recursion(row, col, moves):
            if moves < 0:
                return 0
            if row >= m or row < 0 or col >= n or col < 0:
                return 1
            if dp[row][col][moves] != -1:
                return dp[row][col][moves]
            up = recursion(row-1, col, moves-1)
            down = recursion(row+1, col, moves-1)
            left = recursion(row, col-1, moves-1)
            right = recursion(row, col+1, moves-1)
            
            dp[row][col][moves] = up+down+left+right
            return dp[row][col][moves]
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        return (recursion(startRow, startColumn, maxMove))%mod