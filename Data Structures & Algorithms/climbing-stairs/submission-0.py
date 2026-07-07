class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n <= 2:
                return n
            if n in memo:        
                return memo[n]
            
            memo[n] = helper(n - 1) + helper(n - 2)  
            return memo[n]

        return helper(n)