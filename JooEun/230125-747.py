# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        F_lst = [0, 0 ]

        for i in range (2, len(cost)+1):
            x = F_lst[i-2] + cost[i-2]
            y = F_lst[i-1] + cost[i-1]
            F_lst.append(min(x,y))
        
        return F_lst[-1]
