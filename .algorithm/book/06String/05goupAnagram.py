# leetcode 49
# https://leetcode.com/problems/group-anagram/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)  # set default type of element
        for word in strs:
            # 파이썬은 C언어를 통해 "팀소트" 정렬을 사용하여 퀵&병합 정렬보다 속도가 더 빠르다!
            anagrams["".join(sorted(word))].append(word)
        # in python3, dictionary.values() returns "view", so it need to be transfored into list
        return list(anagrams.values())
