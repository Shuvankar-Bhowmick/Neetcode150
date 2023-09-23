"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict()
        tickets.sort()
        res = []
        # building the adjacency list using the sorted tickets list
        for src, des in tickets:
            adj[src].append(des)

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if adj[src] == []:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                # Pop the node from the adj list
                adj[src].pop(i)
                # Append the same in the result list
                res.append(v)
                if dfs(v):
                    return True

                # Backtrack
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res
