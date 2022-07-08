class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """i = 0
        m, n = len(matrix), len(matrix[0])
        j = n - 1
        
        while (i >= 0 and i < m) and (j >= 0 and j < n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False"""
        
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        lo, hi = 0, (n*m) - 1
        while lo <= hi:
            mid = (lo + (hi - lo) // 2)
            if matrix[mid//m][mid%m] == target:
                return True
            if matrix[mid//m][mid%m] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False