'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i , j = 0, 1
        while (j < len(prices)):
            # i: buy, j: sell
            # i must always be < j
            if prices[i] <= prices[j]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                i = j 

            j += 1
        return maxProfit