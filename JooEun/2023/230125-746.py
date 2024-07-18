# https://leetcode.com/problems/min-cost-climbing-stairs/
# DP

# My solution
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        F_lst = [0, 0 ]

        for i in range (2, len(cost)+1):
            x = F_lst[i-2] + cost[i-2]
            y = F_lst[i-1] + cost[i-1]
            F_lst.append(min(x,y))
        
        return F_lst[-1]

# Other's solution 1
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])

            
# Other's solution 2
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost)<3:
            return min(cost)
        cost[0], cost[1] = cost[0], min(cost[1], cost[0]+cost[1])
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-2], cost[i-1]) + cost[i]
        return cost[-1]
