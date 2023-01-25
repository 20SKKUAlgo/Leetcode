# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        f_lst = [1,1]
        for i in range(2,n+1):
            n_f = f_lst[i-1]+f_lst[i-2]
            f_lst.append(n_f)
        
        return f_lst[n]
