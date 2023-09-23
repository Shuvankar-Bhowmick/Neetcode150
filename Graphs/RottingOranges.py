'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        def bfs():
            time = 0
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            while fresh > 0 and q:

                qLen = len(q)
                for i in range(qLen):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (r in range(rows) and
                            c in range(cols) and
                            grid[r][c] == 1
                            ):
                            q.append((r, c))
                            grid[r][c] = 2
                            fresh -= 1
                time += 1

            return time if fresh == 0 else -1
        return bfs()
