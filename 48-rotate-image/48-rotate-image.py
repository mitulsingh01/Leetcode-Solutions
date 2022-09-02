class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def swap(mat, i, j):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        n = len(mat)
        for i in range(n):
            for j in range(i):
                swap(mat, i, j)
        for i in range(n):
            mat[i].reverse()
        return mat
        
        """left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                
                #save top left element
                topLeft = matrix[top][left + i]
                
                #bottomLeft = TopLeft
                matrix[top][left + i] = matrix[bottom - i][left]
                
                #move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                #top right  = bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                #top left into top right
                matrix[top + i][right] = topLeft
                
            left += 1
            right -= 1"""