# https://leetcode.com/problems/integer-replacement/description/
# Greedy, DP
# recursive 

class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}; dp[0] = 0; dp[1] = 0
        def recur(n):
            if n in dp:
                return dp[n]
            if (n % 2 == 0):
                return 1 + recur(n//2)
            else:
                return 1 + min(recur(n-1), recur(n+1))
        return recur(n)