'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        # By default we are always going to put the number in the maxHeap
        heapq.heappush(self.maxHeap, -num)
        if (len(self.maxHeap) > len(self.minHeap) + 1 or 
            (self.minHeap and self.minHeap[0] < -self.maxHeap[0])
            ):
            num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -num)
            if len(self.minHeap) > len(self.maxHeap) + 1:
                num2 = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -num2)

    def findMedian(self) -> float:
        totalLength = len(self.maxHeap) + len(self.minHeap)
        ans = 0
        if not totalLength % 2:
            ans = (self.minHeap[0] - self.maxHeap) / 2
        else: 
            ans = self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        return ans
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()