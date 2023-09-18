'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pcf, atl = set(), set()

        for c in range(cols):
            dfs(0, c, pcf)
            dfs(rows-1, c, atl)

        for r in range(rows):
            dfs(r, 0, pcf)
            dfs(cols-1, c, atl)

        def dfs(row, col, visit):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            visit.add((row, col))

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    (r, c) not in visit and
                        heights[row][col] <= heights[r][c]):
                    dfs(r, c, visit)

        res = []

        for i in range(rows):
            temp = []
            for j in range(cols):
                if heights[i][j] in pcf and heights[i][j] in atl:
                    temp.append(heights[i][j])
            res.append(temp)

        return res
