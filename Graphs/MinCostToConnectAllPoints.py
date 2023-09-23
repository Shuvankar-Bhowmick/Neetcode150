'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points
'''
import collections
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        neighbors = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                dist = manhattan(points[i], points[j])
                neighbors[i].append([j, dist])
                neighbors[j].append([i, dist])
            
            
        def bfs():
            minH = [(0, 0)] # priority queue
            visited = set()
            minCost = 0
            
            while len(visited) < n:
              dist, node = heapq.heappop(minH)
              if node in visited:
                  continue
              
              minCost += dist
              visited.add(node)
              for nei, cost in neighbors[node]:
                  if nei not in visited:
                      heapq.heappush(minH, (cost, nei))
                      
            return minCost
        
        return bfs()       
                    