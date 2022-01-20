# leetcode 344
# https://leetcode.com/problems/reverse-string/
# 주어진 문자열을 뒤집는 함수를 작성하라.
# 리턴 없이 리스트 내부를 직접 조작하여 공간복잡도를 O(1)로 작성한다.

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
    	return self.usingReverse(s)
        
    # 투포인터 사용 : 212ms
    def usingTwoPointer(self, s: str) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # 리스트의 reverse 사용 : 188ms
    # reversed(s)의 경우 s를 조작하지 않음(다른 레퍼런스를 가리키게 됨) + 속도도 느림
    def usingReverse(self, s: str) -> None:
    	s.reverse()

    # 슬라이싱 사용 : 200ms
    # 문자열의 경우 바로 [::-1]이 작동하나, 
    # 실행 환경에 따라 리스트에서는 s[:] = s[::-1]로 작성해야 작동할 수도 있음.
    def usingSlicing(self, s: str) -> bool:
    	s[:] == s[::-1]