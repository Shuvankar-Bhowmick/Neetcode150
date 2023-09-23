'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''


import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            count = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    i, j = row + dr, col + dc
                    if (i in range(rows) and
                            j in range(cols) and
                            grid[i][j] == 1 and
                            (i, j) not in visited
                            ):
                        q.append((i, j))
                        visited.add((i, j))
                        count += 1

            return count

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if ((i, j) not in visited and grid[i][j] == 1):
                    ans = max(ans, bfs(i, j))
        return ans
