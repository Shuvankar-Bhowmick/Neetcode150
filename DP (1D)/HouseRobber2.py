class Solution:
    def robHouses(self, nums, start, end):
        rob1 = nums[start]
        rob2 = max(nums[start + 1], rob1)
        
        for i in range(start + 2, end):
            temp = rob2
            rob2 = max(nums[i] + rob1, rob2)
            rob1 = temp
        return max(rob1, rob2)        

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        maxRob = max(self.robHouses(nums, 0, n-1), self.robHouses(nums, 1, n))
        return maxRob

    