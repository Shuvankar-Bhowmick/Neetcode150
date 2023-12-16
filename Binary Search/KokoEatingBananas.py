'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

'''
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the total hours required for any particular speed
        # If the time required is 
        l, r = 1, max(piles)
        ans = 0

        while l <= r:
            k = l + (r - l) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / k)

                if totalTime <= h:
                    ans = r
                    r = k - 1
                else:
                    l = k + 1    
            
        return ans    

solution = Solution()
print(solution.minEatingSpeed([30,11,23,4,20],5))        
                
