# This one is an implementation of the Bellman Ford algorithm

'''
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''
from typing import List, Self


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # No need for an adjancency list for this algorithm

        # Implement the actual algorithm
        def findCheapestFlight(k):
            prices = [float("inf")] * n
            prices[src] = 0
            pricesTemp = prices[:]  # copying the prices list

            while (k + 1 > 0):

                for frm, to, price in flights:
                    cost = prices[frm]
                    if (prices[frm] != float("inf") and
                            cost + price < pricesTemp[to]):
                        pricesTemp[to] = price + cost

                prices = pricesTemp[:]
                k -= 1
            return prices[dst] if prices[dst] != float("inf") else -1

        res = findCheapestFlight(k)

        # For testing, don't copy this
        print(f"Minimum price to reach the destination is {res}")

    findCheapestPrice(Self, 4,
                      [[0, 1, 100], [1, 2, 100], [2, 0, 100],
                       [1, 3, 600], [2, 3, 200]],
                      0,
                      3,
                      1)
