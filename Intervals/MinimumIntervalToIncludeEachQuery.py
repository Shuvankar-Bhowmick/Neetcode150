'''
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
'''
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        res, i = {}, 0
        intervals.sort()
        
        for query in sorted(queries):
            query = queries[i]
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            res[query] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
print(Solution().minInterval([[4,5],[5,8],[1,9],[8,10],[1,6]],
[7,9,3,9,3]))