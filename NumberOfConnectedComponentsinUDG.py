'''
In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

You need to return the number of connected components in that graph.

Example 1

Input:

3
[[0,1], [0,2]]
Output:

1
Example 2

Input:

6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:

2
'''
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        # We will be using union find here
        parent = [i for i in range(n)]
        rank = [1] * n
        count = n
        
        def find(n):
            res = n
            
            while res != parent[res]:
                # path compression
                res = parent[parent[res]]
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2: return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return 1                
        
        for u, v in edges:
            count -= union(u, v)
        return count        