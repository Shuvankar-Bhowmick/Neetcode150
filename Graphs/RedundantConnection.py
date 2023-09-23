"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
"""

from typing import List


def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # In this code we will be using the union find alogrithm
    visited = set()
    parent = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)
    ans = []

    # Function to find the parent of a node n
    def find(n):
        res = n
        while res != parent[res]:
            # path compression
            parent[res] = parent[parent[res]]
            res = parent[res]

        return res

    # Function to merge (union) two nodes
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            ans.append(n1)
            ans.append(n2)
            return False

        if rank[p1] > rank[p2]:
            # p2 must be merged as a child of p1
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            # p1 must be merged as child of p2
            parent[p1] = p2
            rank[p2] += rank[p1]

        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            break

    return ans
