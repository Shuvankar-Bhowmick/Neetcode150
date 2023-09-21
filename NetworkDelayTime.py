'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}
        for u, v, w in times:
            adj[u].append([v, w])
        
        # Will apply the Dijkstra's algorithm here
        def bfs():
            minH = [(0, k)]
            visited = set()
            time = 0
            while minH:
                t, node = heapq.heappop(minH)
                if node in visited:
                    continue
                
                visited.add(node)
                time = t # time is the min distance of current node from source node
                for nei, wei in adj[node]:
                   if nei not in visited: 
                    heapq.heappush(minH, (time + wei, nei))
                
            return time if len(visited) == n else -1
        
        return bfs()                
            