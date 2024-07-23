# https://leetcode.com/problems/ransom-note/description/
# hash table

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        for key, value in ran.items():
            if(value > mag[key]):
                return False

        return True