from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # store the top left in a variable
                topLeft = matrix[top][l + i]
                # shift the bottom left to the top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # shift the bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # shift the top right to the bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # shift the top left to the top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1    
        