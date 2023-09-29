'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''

from cmath import inf
import collections
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = r = 0
        result = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            result += 1 
        
        return result        

    # alternate solutions (long-ass)
    """
        if len(nums) <= 1: return 0

        q = collections.deque()
        n = len(nums)
        count = 0
        minCount = inf

        q.append((nums[0], 0))
        i = 1
        while q:
            length = len(q)
            count += 1
            for j in range(length):
                jumpLength, index = q.popleft()

                limit = index + jumpLength

                if limit >= n - 1: 
                    minCount = min(minCount, count)    
                    continue

                while i <= limit:
                    q.append((nums[i], i))
                    i += 1
        return int(minCount) 
     """           
