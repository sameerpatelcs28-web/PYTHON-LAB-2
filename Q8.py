class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])

        left, right = 0, n*m - 1

        while left <= right:
            mid = (left + right) // 2
            
            # convert 1D index → 2D index
            r = mid // m
            c = mid % m

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
