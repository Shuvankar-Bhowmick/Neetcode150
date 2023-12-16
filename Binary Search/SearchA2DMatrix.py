from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, (rows * cols) - 1
        while l <= r:
            mid = (l + r) // 2 # integer division
            r = mid // rows
            c = mid % rows

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False            
