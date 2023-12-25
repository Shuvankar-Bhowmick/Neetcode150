'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ans = []

        while top < bottom and left < right:
            # print every i in the top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            # print every i in the right column
            for j in range(top, bottom):
                ans.append(matrix[j][right - 1])
            right -= 1
            if (top >= bottom or left >= right):
                break

            # print every i in the bottom row
            for k in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][k])
            bottom -= 1
            # print every i in the left column
            for l in range(bottom - 1, top - 1, -1):
                ans.append(matrix[l][left])
            left += 1
        return ans    
    
solution = Solution()
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))    