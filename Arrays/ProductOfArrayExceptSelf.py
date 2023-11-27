from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for i in range(len(nums))]
        # Find the product of the nums list
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        
        prefix[0], suffix[-1] = nums[0], nums[-1]
        # calculate the prefix product
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        # calculate the suffix product
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j]
        ans[0] = suffix[1]
        ans[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            ans[i] = prefix[i - 1] * suffix[i + 1]
            
        return ans       