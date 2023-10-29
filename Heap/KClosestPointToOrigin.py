'''
link: https://leetcode.com/problems/k-closest-points-to-origin/description/
APPROACH 1: Approach is pretty simple.
    1. We will find out the distance of each point from the origin and store it along with it's coordinates
       in a min heap in the form of a tuple
    2. Then we will loop the min heap for k times and append the second value of the tuple to our answer list 😀   
APPROACH 2: Apply quicksort/quickselect    
dist(nums[i]) = x**2 + y **2, pivot = dist(nums[r])
compare between nums[i] and pivot and sort the nums array 

OBSERVATION: On theory the quickselect algorithm is supposed to run faster than the min heap one, but p]ractically the reverse happens as the min heap takes an approx of 750ms while the quickselect (iterative) one takes around 960-1000 ms. 

REASON: This is most probably due to the distribution of the array where sometimes the array might be in a sorted state thereby increasing the time complexity to O(n^2) (worst case), the only reason the code is still working for a large input is because the pivot has been randomized which reduces the possible bottleneck that may arise due to this condition. 

RECOMMENDATION: Use the min heap approach (Approach 1) in interviews as it takes less time and is easily readable, if the interviewer asks for a more optimized solution (theoretically) thereafter, then explain to him Approach 2
'''
import heapq
import math
import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # using min-heap/priority queue
        """ 
        minHeap = []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)            
            heapq.heappush(minHeap, (dist, [x, y]))

        while k > 0 and minHeap:
            dist, coord = heapq.heappop(minHeap)
            res.append(coord)
            k -= 1

        return res    
     """
        
        # using quicksort
        if k < len(points):
            self.KClosestHelper(0, len(points) - 1, points, k)
        return points[: k]
    
    def KClosestHelper(self, start, end, points, k):
        
        while start <= end:
            pIndex = self.partition(start, end, points)

            if pIndex == k: return True
            elif pIndex > k:
                end = pIndex - 1
            else:
                start = pIndex + 1
        
    
    def partition(self, start, end, points):
        # ///////////////////////////////////////////
        # using randomized pivot so as to reduce the time complexity even more
        randIndex = random.randint(start, end)
        points[end], points[randIndex] = points[randIndex], points[end]
        pivot = points[end]
        # ///////////////////////////////////////////

        temp = start
        for i in range(start, end):
            if self.dist(points[i]) < self.dist(pivot):
                points[temp], points[i] = points[i], points[temp]
                temp += 1

        points[temp], points[end] = pivot, points[temp]
        return temp

    def dist(self, arr): 
        return arr[0] ** 2 + arr[1] ** 2    
        
        

        