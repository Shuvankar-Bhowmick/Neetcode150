'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''
import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = collections.deque()
        l = r = 0

        for r in range(len(nums)):
            # check if the queue is having any smaller values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # check if leftmost element in the deque is inside window or not
            if q[0] <= r - k:
                q.popleft()
            if r >= k - 1: 
                ans.append(nums[q[0]])
        return ans