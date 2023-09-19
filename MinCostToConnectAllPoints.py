'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # First make the adjacency list
        # Then code the Prim's algorithm

        visited = set()
        n = len(points)

        # the adjacency list
        adj = {i: [] for i in range(n)}  # adj = [cost, node]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n + 1):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append(cost, j)
                adj[j].append(cost, i)

        # prim's algorithm
        cost = 0
        res = []
        minH = [[0, 0]]

        def prim():
            while len(visited) < n:
                cost, node = heapq.heappop(minH)
                if node in visited:
                    continue
                res += cost
                for dist, nei in adj[node]:
                    if nei not in visited:
                        heapq.heappush([dist, nei])

        return res
