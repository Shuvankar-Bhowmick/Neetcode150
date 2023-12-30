'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        first = 0

        # check the columns
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        # check the rows
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        # check for the [0, 0] element
        if first == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        print(matrix)

solution = Solution()
print(solution.setZeroes([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]))                  
        