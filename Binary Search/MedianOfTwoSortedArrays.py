'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
from typing import List


class Solution:    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Find out if the array is odd or even
        m, n = len(nums1), len(nums2)
        if not n and not m: return 0
        
        half = (n + m) // 2
        # 2. By convention we always make nums2 as the smaller array
        if n > m:
            nums1, nums2 = nums2, nums1   
            m, n = n, m
        # 3. Now we search the smaller array (nums2)
        start, end = 0, len(nums2) - 1
        ans = 0
        while True:
            #  4. i1: end index of left partition of first array
            #     i2: end index of left partition of second array
            i2 = (start + end) // 2
            i1 = half - i2 - 2

            left1, right1 = nums1[i1] if i1 >= 0 else float('-inf'), nums1[i1 + 1] if i1 < m - 1 else float('inf')
            left2, right2 = nums2[i2] if i2 >= 0 else float('-inf'), nums2[i2 + 1] if i2 < n - 1 else float('inf')

            if (left1 <= right2 and left2 <= right1):
                ans = (min(right1, right2) 
                        if (n + m) % 2 != 0 
                        else (max(left1, left2) + min(right1, right2)) / 2)
                break
            
            if left1 > right2:
                start = i2 + 1
            if left2 > right1:
                end = i2 - 1

        return ans 

    """ def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
 """
solution = Solution()
print(solution.findMedianSortedArrays([1,3],[2]))             
print(solution.findMedianSortedArrays([1,2],[3,4]))
print(solution.findMedianSortedArrays([],[1]))
                    

        
        
        