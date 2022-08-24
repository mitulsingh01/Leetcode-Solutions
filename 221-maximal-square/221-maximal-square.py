class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) not in cache:
                down, right, diag = helper(r+1, c), helper(r, c+1), helper(r+1, c+1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diag)
            return cache[(r,c)]
            
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        helper(0, 0)
        return max(cache.values()) ** 2
        