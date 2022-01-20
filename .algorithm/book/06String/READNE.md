#### string, palindrome 문제 관련

- 전처리 : list(**map**(**lambda x: x.lower()**, **filter**(lambda x: x.isalnum(), s)))
- list의 pop은 O(n^2)이지만 Deque의 pop은 O(n)
- 파이썬의 **슬라이싱**은 C로 구현되어있어 훨씬 빠르다. palindrome 비교 시 list[::-1] 추천
- 실행 환경에 따라 list = list[::-1]가 동작하지 않으면 list[:] = list[::-1] 사용해야 할 수도
- reversed(s)는 s 조작 대신 복사하여 새로운 객체 반환, 느림
- s.reverse()는 s 자체를 조작하며, 더 빠름. 그러나 슬라이싱이 제일 빠름!
- 숫자, 문자, alnum 판별
  - string.isdecimal() => int형으로 변환이 가능한가? 특수문자 포함되면 무조건 False
  - string.**isdigit()** => 정수 모양으로 보이는가? 숫자로 보이는 특수문자는 포함되어도 True (ex : 2¹²³⁴⁵⁶는 True, ½는 False)
  - string.isnumeric() => 숫자 값으로 표현되는가? 제곱근, 분수, 거듭제곱 등의 특수문자가 포함되어도 True (ex: ½도 True)
  - string.isalpha()
  - string.isalnum()
- string.split()은 빈칸이 여럿 있어도 무시 : "a a"는 ["a", "", "a"]가 아니라 ["a", "a"] 반환
- max 함수는 가장 큰 값을 반환, key **함수**를 통해 기준 설정 가능 : max(counts, key=counts.get)
- most_common(n)은 collections.Counter의 빈도가 높은 n개의 (데이터, 개수) 쌍을 정렬된 리스트로 반환
- dictionary.values()는 View 객체이므로 list로 감싸주어야 배열 형태로 반횐됨
- palindrome 판별을 위해 투포인터 사용하기도.
  - 홀수개의 단어인지 짝수개의 단어인지에 따라 확장, 축소 등을 다르게 처리해주어야 함.
