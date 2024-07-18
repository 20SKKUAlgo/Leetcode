# https://leetcode.com/problems/lemonade-change/
# Greedy
# 첫번째 접근법: 리스트, 이중 반복문, deep copy => Time exceed
# 두번째 접근법: 해시, 반복문 => 통과

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lst= []
        dic = dict({5: 0, 10: 0, 20: 0})

        for i in bills:
            tmp = i
            if (i == 5):
                dic[5] += 1
            else:
                tmp -= 5
                if (tmp == 5):
                    if (dic[5] == 0):
                        return False
                    else:
                        dic[5] -= 1
                elif (tmp == 15):
                    if (dic[10] == 0 and dic[5] >= 3):
                        dic[5] -= 3
                    elif (dic[10] > 0 and dic[5] > 0):
                        dic[5] -= 1
                        dic[10] -= 1
                    else:
                        return False
                dic[i] += 1
        
        return True
