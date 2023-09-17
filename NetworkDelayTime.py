'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

'''
import heapq
from typing import List, Self


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list cuz these buggers don't do it
        adj = {i: [] for i in range(n + 1)}
        for u, v, w in times:
            adj[u].append([v, w])
            # adj[v].append([u, w])

        visited = [float("inf")] * (n + 1)
        # implement the dijkstra's algorithm

        def dijkstra():
            cost = 0
            minH = [(0, k)]
            visited[k] = 0
            print(f"Current length of heap: {len(minH)} \n")

            while (len(minH) > 0):
                dist, node = heapq.heappop(minH)

                for v, w in adj[node]:
                    if dist + w < visited[v]:
                        visited[v] = dist + w
                        heapq.heappush(minH, (dist + w, v))

            for v in range(1, len(visited)):
                if visited[v] == float("inf"):
                    return -1
                cost = max(cost, visited[v])

            return cost
        ans = dijkstra()
        print(f"Minimum cost: {ans}")
        return ans
    networkDelayTime(Self, [[1, 2, 1]], 2, 2)
