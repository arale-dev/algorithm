# leetcode 125
# https://leetcode.com/problems/valid-palindrome/
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 특수문자 및 공백은 무시한다.

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	return self.usingSlicing(s)
    	# return self.usingList(s)
    	# return self.usingDeque(s)
        
    # 리스트 사용 : 52ms
    def usingList(self, s: str) -> bool:
    	s = list(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))
        n = len(s)

        for i in range(n // 2):
            if (s[i] != s[n-i-1]):
                return False

        return True

    # 데크 사용 : 52ms
    # list의 pop은 O(n^2)이지만 Deque의 경우 O(n)
    # list의 element 접근과 동일하게 O(n)으로 비슷한 속도!
    def usingDeque(self, s: str) -> bool:
    	import collections
    	strs = collections.deque()


        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
        	if strs.popleft() != strs.pop():
        		return False
        return True

    # 슬라이싱 사용 : 32ms
    # 정규식을 통한 필터링, 슬라이싱 사용
    # 슬라이싱은 C로 구현되어있어 훨씬 빠르다
    def usingSlicing(self, s: str) -> bool:
    	import re
    	s = re.sub('[^0-9a-zA-Z]', '', s)
    	s = s.lower()
    	return s == s[::-1]