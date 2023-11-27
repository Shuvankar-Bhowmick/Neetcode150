'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        res = []
        # Every value at an index in count is an array of elements that have the specific count.
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counter[n] += 1

        for key, value in counter.items():
            count[value].append(key)

        i = len(count) - 1
        while k > 0 and i > 0:
            for c in count[i]:
                res.append(c)
                k -= 1
            i -= 1
        return res

obj = Solution()
obj.topKFrequent([1,1,1,2,2,3],2)
obj.topKFrequent([1],1)