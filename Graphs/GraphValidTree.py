'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
'''

from collections import defaultdict
from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        visited = set()
        neighbour = defaultdict(list)
        for u, v in edges:
            neighbour[u].append(v)
            neighbour[v].append(u) # since the edges are not directed
            
        
        def dfs(node, prev):
            
            if len(visited) == n: return True
            if node in visited: return False
            visited.add(node)
            
            for nei in neighbour[node]:
                if nei != prev:
                    if not dfs(nei, node): return False 
                    
            return True
        return dfs(0, -1) and len(visited) == n
                