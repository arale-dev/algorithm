# leetcode 5
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.
# # Input: s = "babad"
# # Output: "bab"
# # Note: "aba" is also a valid answer.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # edge case check
        if len(s) <= 1 or s == s[::-1]:
            return s

        answer = ''
        for i in range(len(s)):
            # palindrome can have center character(case 1) or not(case 2)
            case1 = self.getLongestPalindrome(s, i, i+2)
            case2 = self.getLongestPalindrome(s, i, i+1)
            answer = max(answer, case1, case2, key=len)

        return answer

    def getLongestPalindrome(self, s: str, left: int, right: int) -> str:
        # 투포인터를 슬라이딩 윈도우처럼 사용. left와 right의 문자가 동일하면 확장하여 재확인
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]  # 첫번째 ~ 세번째 문자까지 반환 시, left = -1, right = 3인 상태
