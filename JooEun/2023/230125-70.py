# https://leetcode.com/problems/climbing-stairs/
# Dynamic programming

# my solution
class Solution:
    def climbStairs(self, n: int) -> int:
        f_lst = [1,1]
        for i in range(2,n+1):
            n_f = f_lst[i-1]+f_lst[i-2]
            f_lst.append(n_f)
        
        return f_lst[n]

 
# other's solution
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for i in range(n):
            a,b = b,a+b
        return a
