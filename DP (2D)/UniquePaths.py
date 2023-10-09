'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        # using memoization
        """ grid = [[0] * n for _ in range(m)]    

        def dfs(r, c):
            if r == rows or c == cols:
                return 0
            if grid[r][c] > 0:
                return grid[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            grid[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return grid[r][c]
        
        return dfs(0, 0) """

        # using bottom-up approach for dynamic programming using tabulation method
        prevRow = [0] * n

        for i in range(rows - 1, -1, -1):
            currRow = [0] * n
            currRow[n - 1] = 1
            for j in range(cols - 2, -1, -1):
                currRow[j] = prevRow[j] + currRow[j + 1]
            prevRow = currRow    

        return prevRow[0]    