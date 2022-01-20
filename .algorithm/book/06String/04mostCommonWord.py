# leetcode 819
# https://leetcode.com/problems/most-common-word/

# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique. => 동일한 갯수의 처리 고려할 필요 없음

# The words in paragraph are case-insensitive and the answer should be returned in lowercase. => lower로 전처리한 이후 사용할 것
# Punctuation is ignored => 문장부호는 무시되니 전처리 필요

# # # Python의 Comprehension : https://mingrammer.com/introduce-comprehension-of-python/ 참고

from typing import Collection, List
import re
import collections


class Solution:
    # Comprehension, 정규식 표현, Counter 객체 사용 : 36ms
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 전처리
        # split에 seperator을 지정하지 않으면 공백 처리를 알아서 진행
        # 'a  a'.split => ['a', '', 'a'] 가 아닌 ['a', 'a']를 반환
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]

        return self.usingDict(words)

    # 36ms
    def usingDict(self, words: List[str]) -> str:
        counts = Collection.defaultdict(int)  # 키 존재 유무 확인 패스
        for word in words:
            counts[word] += 1

        # max 함수는 가장 큰 값을 반환, key 함수를 통해 기준 설정 가능
        # => key=counts.get 으로 설정해도 동일. 각 원소를 돌면서 실행
        return max(counts, key=lambda x: counts[x])

    # 36ms
    def usingCounter(self, words: List[str]) -> str:
        # most_common(n)은 빈도가 높은 n개의 (데이터, 개수) 쌍을 정렬된 리스트로 반환
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
