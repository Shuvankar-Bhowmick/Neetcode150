'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # In this solution I will apply a BFS algorithm

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = set()
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            q.append([i, j])
            count = 0

            while q:
                row, col = q.popleft()

                if (row, col) in visited:
                    continue

                visited.add((row, col))
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r, c) not in visited and
                            r in range(0, rows) and
                            c in range(0, cols) and
                            grid[r][c] != '0'
                            ):
                        q.append([r, c])

            # all 1's are over here, count of land increases by one
            return 1

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if ((i, j) not in visited and
                        grid[i][j] != '0'
                        ):
                    ans += bfs(i, j)

        return ans
