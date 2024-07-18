# 2023.01.10 https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        for i in range(len(xStr)//2):
            if(xStr[i] != xStr[len(xStr)-1-i]):
                return False
        
        return True
