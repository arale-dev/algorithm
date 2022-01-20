# leetcode 937
# https://leetcode.com/problems/reorder-data-in-log-files/

# logs 리스트가 입력으로 주어지며, 각 원소 log는 띄어쓰기로 구분된 string이다.
# 첫번째 단어는 identifier이며 log는 letter-logs 또는 digit-logs일 수 있다.
# # # Letter-logs: All words (except the identifier) consist of lowercase English letters.
# # # Digit-logs: All words (except the identifier) consist of digits.

# 아래 룰에 맞도록 리스트를 재정렬 하여라.
# # # The letter-logs come before all digit-logs.
# # # The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# # # The digit-logs maintain their relative ordering. => 상대적인 순서를 유지하는 것이므로, 정렬 상태를 조작하지 말 것

from typing import List


class Solution:
    # 람다 표현식과 split, sort(key 설정) : 36ms
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []

        # string.isdecimal() => int형으로 변환이 가능한가? 특수문자 포함되면 무조건 False
        # string.isdigit() => 정수 모양으로 보이는가? 숫자로 보이는 특수문자는 포함되어도 True (ex : 2¹²³⁴⁵⁶는 True, ½는 False)
        # string.isnumeric() => 숫자 값으로 표현되는가? 제곱근, 분수, 거듭제곱 등의 특수문자가 포함되어도 True (ex: ½도 True)
        for log in logs:
            if log.split()[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)

        # string.split(sep, maxsplit) => 한번만 나누고 싶을 때에는 maxsplit 주기
        letterLogs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        return letterLogs + digitLogs
