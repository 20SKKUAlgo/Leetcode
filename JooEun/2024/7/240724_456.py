# https://leetcode.com/problems/132-pattern/
# stack, bst
# not solved

class Solution:
    def find_index(self, lst, value):
        return lst.index(next(filter(lambda x: x[1] == value, lst)))

    def find132pattern(self, nums: List[int]) -> bool:
        lst = []
        for index, item in enumerate(nums):
            lst.append((item, index))
        lst = sorted(lst, key = lambda x: (x[0], x[1]))
        print(lst)
        for i in range(len(nums)-2):
            first, second, third = self.find_index(lst, i), self.find_index(lst, i+1), self.find_index(lst, i+2)
            print(f"{first} {third} {second}")
            if (first <= third <= second and lst[first][0] < lst[third][0]):
                return True
        return False
        
            