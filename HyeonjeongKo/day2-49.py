class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) # 빈 리스트

        # 각 단어를 정렬한값을 키로사용
        # 원래단어를 value로 사용
        for word in strs:
            # 파이썬은 list는 키값이될수없음.
            # 따라서 join을 사용해 str키값으로 반환
            anagrams[''.join(sorted(word))].append(word) 
        return list(anagrams.values())
