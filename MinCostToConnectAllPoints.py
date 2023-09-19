<<<<<<< HEAD
"""
=======
'''
>>>>>>> 5e14e1941618a0db293c3e41195d311b0d4ef7eb
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
<<<<<<< HEAD
"""
=======

'''
>>>>>>> 5e14e1941618a0db293c3e41195d311b0d4ef7eb

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
<<<<<<< HEAD
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
=======
        # First we need to create an adjacency list
        adj = {i:[] for i in range(len(points))}
        visited = set()
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range (i+1, range(len(points))):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Minimun spanning tree algorith: Prim's algorithm
        def mst():
            minH = [[0, 0]]
            res = 0
            while (len(visited) < len(points)):
>>>>>>> 5e14e1941618a0db293c3e41195d311b0d4ef7eb
                cost, node = heapq.heappop(minH)
                if node in visited:
                    continue
                res += cost
<<<<<<< HEAD
                for dist, nei in adj[node]:
                    if nei not in visited:
                        heapq.heappush([dist, nei])

        return res
=======
                visited.add(node)
                for dist, nei in adj[node]:
                    if nei not in visited:
                        heapq.heappush(minH, [dist, nei])

            return res

        return mst()            


>>>>>>> 5e14e1941618a0db293c3e41195d311b0d4ef7eb
