# https://leetcode.com/problems/di-string-match/
# Greedy
# 첫번째 시도: 리스트 append연산만, start=0, end=len(s)로 양쪽에서 값 할당하는 전략

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)
        lst = []
        for i in s:
            if i == "I":
                lst.append(start)
                start += 1
            else:
                lst.append(end)
                end -= 1
        lst.append(start)
        return lst        