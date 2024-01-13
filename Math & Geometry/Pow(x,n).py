class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0

        ans = self.searchPow(x, abs(n))
        return ans if n > 0 else (1 / ans)  
    
    def searchPow(self, x: float, n: int):
        # base cases
        if n == 0: return 1
        if n == 1: return x

        # recursion
        ans = self.searchPow(x, n // 2)
        return ans * ans * (x if n % 2 != 0 else 1)
    
solution = Solution()
print(solution.myPow(2.00000,10))
print(solution.myPow(2.00000,-2))
print(solution.myPow(0.44528,0))