# https://leetcode.com/problems/wiggle-subsequence/
# Greedy
# 숫자 리스트, 반복문

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prev = nums[0]
        lst = [nums[0]]
        # up down up down
        for i in range(1, len(nums)):
            if ( len(lst)%2 == 0):
                if(prev > nums[i]):
                    lst.append(nums[i])
                    prev = nums[i]
                elif(prev < nums[i]):
                    lst[-1] = nums[i]
                    prev = nums[i]
            else:
                if(prev < nums[i]):
                    lst.append(nums[i])
                    prev = nums[i]
                elif(prev > nums[i]):
                    lst[-1] = nums[i]
                    prev = nums[i]

        # down up down up
        prev = nums[0]
        lst2 = [nums[0]]
        for i in range(1, len(nums)):
            if (len(lst2)%2 == 0):
                if(prev < nums[i]):
                    lst2.append(nums[i])
                    prev = nums[i]
                elif(prev > nums[i]):
                    lst2[-1] = nums[i]
                    prev = nums[i]
            else:
                if(prev > nums[i]):
                    lst2.append(nums[i])
                    prev = nums[i]
                elif(prev < nums[i]):
                    lst2[-1] = nums[i]
                    prev = nums[i]
        print(lst)
        print(lst2)
        return max(len(lst), len(lst2))

# 아래는 GPT가 줄여준 코드. 
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n < 2:
            return n
        
        up = down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        
        return max(up, down)