'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # APPROACH 1: T(n) = O(n), S(n) = O(n)
        # Take the max from both left and right, find the min from them and then subtract the 
        # current height from the result thus obtained.
        """ 
        n = len(height)
        suffix = [0] * n
        prefix = [0] * n
        prefix[0] = height[0]
        suffix[n - 1] = height[n - 1] 
        ans = 0

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        for j in range(len(height) - 2 , -1, -1):
            suffix[j] = max(suffix[j + 1], height[j])

        print(f"Prefix: {prefix}")
        print(f"Suffix: {suffix}")

        for i in range(n):
            ans +=  (min(prefix[i], suffix[i]) - height[i] if 
                    min(prefix[i], suffix[i]) - height[i] >= 0 else 0)

        return ans    
 """
        
        # APPROACH 2: T(n) = O(n), S(n) = O(1)
        n = len(height) - 1
        l, r = 0, n
        lMax, rMax = 0, n
        ans = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] <= height[lMax]:
                    ans += height[lMax] - height[l]
                else:
                    lMax = l
                l += 1
            else:
                if height[r] <= height[rMax]:
                    ans += height[rMax] - height[r]
                else:
                    rMax = r
                r -= 1
        return ans        

solution = Solution()
print(solution.trap([4,2,0,3,2,5]))
print(solution.trap([2,0,2]))