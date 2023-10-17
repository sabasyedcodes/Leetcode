class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1]*38
        def solve(n):
            if n == 0:
                return 0
            if n == 1 or n==2:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n] = solve(n-1)+solve(n-2)+solve(n-3)
            return dp[n]
        return solve(n)