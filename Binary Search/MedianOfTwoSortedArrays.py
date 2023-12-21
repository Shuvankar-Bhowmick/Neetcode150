'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Find out if the array is odd or even
        n, m = len(nums1), len(nums2)
        half = (n + m) // 2
        
        # 2. By convention we always make nums2 as the smaller array
        if n < m:
            nums1, nums2 = nums2, nums1
            
        # 3. Now we search the smaller array (nums2)
        start, end = 0, len(nums2) - 1
        while start <= end:
            #  4. i1: end index of left partition of first array
            #     i2: end index of left partition of second array
            i2 = (start + end) // 2
            i1 = half - i2 - 2

            if i2 <= endnums2[i2] <= nums1[i1 + 1]
            
        
        
        