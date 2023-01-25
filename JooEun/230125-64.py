# https://leetcode.com/problems/minimum-path-sum/
# DP

# my solution
import numpy as np

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if(m == 1):
            return sum(grid[0])
        if(n == 1):
            return np.sum(grid)            
        
        lst = [[0 for j in range(n)] for i in range(m)]

        for r in range(m):
            for c in range(n):
                if(r == 0 and c == 0):
                    lst[r][c] = grid[0][0]
                elif(r==0):
                    lst[r][c] = grid[r][c] + lst[r][c-1]
                elif(c==0):
                    # print(str(r) +" "+str(c))
                    lst[r][c] = grid[r][c] + lst[r-1][c]
                else:
                    lst[r][c] = grid[r][c] + min(lst[r-1][c], lst[r][c-1])
        return lst[m-1][n-1]
 
# Other's solution 1
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # current+min(dfs(right),dfs(down))
        r=len(grid)
        c=len(grid[0])

        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    up=0
                    left=0
                else:
                    if i-1<0:
                        up=float('inf')
                    else:
                        up = grid[i-1][j]
                    if j-1<0:                
                        left=float('inf')
                    else:
                        left = grid[i][j-1]
                grid[i][j] = grid[i][j]+min(up,left)
        return grid[-1][-1]
      

# Other's solution 2
"""
Given a `m x n` `grid` filled with non-negative numbers, find a path from top
left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

