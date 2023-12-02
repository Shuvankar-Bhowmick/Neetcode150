'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                maxProfit += prices[i+1] - prices[i]

        return maxProfit  

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))          
print(solution.maxProfit([1,2,3,4,5]))          
print(solution.maxProfit([4,7,1,2]))          