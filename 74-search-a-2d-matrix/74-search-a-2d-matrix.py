class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        m, n = len(matrix), len(matrix[0])
        j = n - 1
        
        while (i >= 0 and i < m) and (j >= 0 and j < n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False