'''
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
'''


from ast import List
import heapq
from typing import Self


class Solution:
    def swimInWater(self, grid) -> int:
        # Need to use a modified version of Dijkstra to solve this problem
        visited = set()
        minH = [(0, 0, 0)]
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def modifiedDijkstra():
            while minH:
                currHeight, row, col = heapq.heappop(minH)

                if (row, col) == (rows-1, cols-1):
                    return currHeight
                if (row, col) in visited:
                    continue
                visited.add((row, col))

                temp = currHeight
                for i, j in directions:
                    r, c = row + i, col + j
                    if (r in range(0, rows) and
                            c in range(0, cols) and
                            (r, c) not in visited
                            ):
                        currHeight = max(temp, grid[r][c])
                        heapq.heappush(minH, (currHeight, r, c)) # type: ignore
                return -1
            
        ans = modifiedDijkstra()
        return ans # type: ignore

    def getAnswer(self):
        ans = self.swimInWater([[0, 2], [1, 3]])
        print(f"Minimum time required: {ans}")


solution = Solution()
solution.getAnswer()
