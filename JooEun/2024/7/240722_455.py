# https://leetcode.com/problems/assign-cookies/description/
# Greedy, easy
# sort list, smallest cookie for smallest greed factored child

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(); s.sort()
        res = 0
        j = 0
        for i in s:
            if j < len(g) and g[j] <= i:
                res += 1
                j += 1
        return res
