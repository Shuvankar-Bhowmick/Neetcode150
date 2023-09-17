import heapq


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        visited = set()
        res = [0 for i in range(V)]
        res[S] = 0

        def dijkstra():
            cost = 0
            minH = [(0, S)]

            while (len(visited) < V):
                dist, node = heapq.heappop(minH)
                if node in visited:
                    continue
                cost = dist
                visited.add(node)
                res[node] = cost
                for edge, weight in adj[node]:
                    heapq.heappush(minH, (weight + cost, edge))
            return res
        return dijkstra()
