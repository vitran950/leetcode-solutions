class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n*m-1

        while left <= right:
            mid = (left + right) // 2
            r = mid // n 
            c = mid % n
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False