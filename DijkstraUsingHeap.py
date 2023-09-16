import heapq


class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        # No need to create an adj list since it has already been given
        minH = []
        res = [float('inf')] * V
        
        heapq.heappush(minH, [0, S])
        res[S] = 0
        def dijkstra():
            while (len(minH) > 0):

                cost, node = heapq.heappop()

                for edge, weight in adj[node]:
                    if weight + cost < res[edge]:
                        heapq.heappush(minH, [weight + cost, edge])
                        res[edge] = weight + cost
        dijkstra()
        return res                