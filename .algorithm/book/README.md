# algorithm

파이썬 알고리즘 인터뷰 정리 및 문제풀이

## 알고리즘을 풀 때에 주의해야할 점 (1~5장 요약)

### 1.파이썬 문법

1. [타입 힌트](#-1.1.-타입-힌트)
2. [컴프리헨션 (List Comprehension, Dict Comp., Set Comp., Generator Expression)](<#-1.2.-컴프리헨션-(list-comprehension,-dict-comp.,-set-comp.,-generator-expression)>)
3. [제너레이터, range](#-1.3.-제너레이터,-range)
4. [여러 함수들 (enumerate, 나눗셈 연산자, print와 string formating, pass, locals, 스타일 가이드)](<#-1.4.-도움이-되는-여러-함수들-(enumerate,-나눗셈-연산자,-print와-string-formating,-pass,-locals,-스타일-가이드)>)

#### 1.1. 타입 힌트

파이썬의 경우 동적 타이핑 언어(인터프리터 언어)임에도 불구하고, 대규모 프로젝트에서도 가독성을 높이기 위한 타입힌트 기능이 있다. (그러나 강제 규약이 아니어서 사용자가 타입 힌트를 보고도 잘못 할당하는 경우가 있을 수 있음. mypy을 설치하여 실행 이전에 확인하는 기능을 사용할 수 있다.)

#### 1.2. 컴프리헨션 (List Comprehension, Dict Comp., Set Comp., Generator Expression)

리스트, 집합, 딕셔너리 등 선언 시, 반복문과 조건문을 생성자 내부에서 사용하여 쉽게 정의하는 것

```python

# 반복 및 조건문
[n*2 for n in range(1, 10+1) if n % 2 == 1] # [2,6,10,14,18]

# if문들은 and로 묶여 모두 만족하는 경우에만 실행
[i for i in range(5) if i%2==0 if i%4==0] # [0,2,4]

# if, else를 함께 쓰는 경우에는 반복문 왼쪽에
[i if i%2==0 else 'odd' for i in range(5)] # [0,'odd',2,'odd',4]

# 다중 조건문 실행결과
[(i,j) for i in range(2) for j in range(3)] # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

# 두가지 모두 동일한 실행 결과를 리턴
[(i,j) for i in range(3) if i%2 == 0 for j in range(3)]
[(i,j) for i in range(3) for j in range(3) if i%2 == 0]
# [(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2)]

# Set, Dict에서도 동일하게 작동한다.
[j for i in range(3) for j in range(3)] # [0, 1, 2, 0, 1, 2, 0, 1, 2]
{j for i in range(3) for j in range(3)} # {0, 1, 2}
{i:j for i in range(3) for j in range(3)} # {0: 2, 1: 2, 2: 2}

# 손쉽게 key와 value를 swap할 수 있다
a = {1: 'one', 2: 'two'}
{value:key for key,value in a.items()} # {'one': 1, 'two': 2}

# Generator도 쉽게 생성할 수 있다.
# 호출 가능한 범위를 벗어나게 되면 StopIteration 에러 발생
gen = (x**2 for x in range(10))
print(gen) # <generator object <genexpr> at 0x105bde5c8>
print(next(gen)) # call 1 # 0
print(next(gen)) # call 2 # 1
# ...
print(next(gen)) # call 11

# Generator Expression으로 생성하는 경우에도,
# yield로 생성하는 일반적인 경우와 똑같이 sum을 사용할 수 있다. (iterable 객체)
gen = (x**2 for x in range(10))
sum_of_squares = sum(gen) # 285
```

#### 1.3. 제너레이터, range

루프의 반복 동작을 제어할 수 있는 루틴 형태. 대량의 값을 생성하는 등의 동작에서 사용된다. 모든 값들을 메모리에 보관하지 않고 제너레이터만을 저장하고 실행시마다 값을 생성해내어 메모리를 크게 아낄 수 있다. yield를 통해 제너레이터 값을 내보낼 수 있으며, 함수는 종료되지 않고 다음 yield가 불리게 되는 때에 다시 실행된다.

```python
def test_generator():
    yield 1
    yield 'string'
    yield True
gen = test_generator()
type(gen) # <class 'generator'>
next(gen) # 1
next(gen) # 'string'
next(gen) # True
next(gen) # StopIteration 에러 발생
```

두 객체는 서로 다른 객체이며, 각기 따로 동작한다.

```python
h = test_generator()
i = test_generator()
h == i # False
h is i # False
next(h) # 1
next(i) # 1
```

range는 제너레이터 방식을 활용하는 대표적인 함수이다. range()를 통해 range 클래스 객체를 생성할 수 있으며, 생성 조건만 정해두고 필요할 때마다 숫자를 생성한다. 아래 두 예시는 서로 다른 방식으로 100만개의 수를 출력하지만 데이터 타입과 메모리 점유율에서 차이가 있음을 알 수 있다. 미리 생성하지 않은 값은 인덱스에 접근 시 바로 생성하도록 구현되어 있기 때문에 리스트와 거의 동일한 느낌으로 사용할 수 있다.

```python
a = [ n for n in range(1000000)]
b = range(1000000)
len(a) # 1000000
len(b) # 1000000
type(a) # <class 'list'>
type(b) # <class 'range'>
b # range(0, 1000000)
import sys
sys.getsizeof(a) # 8448728
sys.getsizeof(b) # 48
```

#### 1.4. 도움이 되는 여러 함수들 (enumerate, 나눗셈 연산자, print와 string formating, pass, locals, 스타일 가이드)

enumerate() : 인덱스와 값 모두 처리하기

```python
a = [2,4,6,8]
for idx,val in enumerate(a):
    print(idx,val)

```

나눗셈 연산자 : //는 몫, %는 나머지를 반환. divmod는 몫과 나머지를 한번에 반환한다.

```python
5 // 3 # 1
5 % 3 # 2
divmod(5,3) # (1, 2)
```

print : sep, end 지정 가능. string formating을 함께 사용하면 더욱 편리하다

```python
print("aa", "bb", "cc", sep="~~", end="@@finish@@")
# aa~~bb~~cc@@finish@@ # 이후 줄바꿈 없이 다음 줄이 연이어서 프린트된다.

idx = 3
val = "three"
print("{0}: {1}".format(idx,val)) # 3: three
print(f"{idx}: {val}") # 3: three
```

pass : 코드의 전체 골격을 잡아놓고 내부 함수들을 나중에 만들기 위해 아무 역할도 하지 않는 널 연산을 반환.

locals : locals()는 현재 로컬 스코프에 정의된 모든 변수를 반환한다. print하여 알고리즘 디버깅 시에 유용하게 사용 가능하다. pprint를 import하여 pprint.pprint(locals())를 통해 예쁘게 정렬된 로컬 변수들을 출력할 수 있다!

인덴테이션 : 파라미터가 시작되는 부분에 맞추거나, 다음 줄과 헷갈리지 않도록 인덴트 추가하기

네이밍 컨벤션 : 스네이크 케이스를 추천

스타일 가이드 : 불명확한 것이 없도록 한다. 함수의 변수 기본값으로 mutable한 객체를 사용하는 대신 immutable 객체 사용하기, True False 판별 시에는 implicit한 방법으로 간결하게 표현하기

```python
# Good
def foo(a, b=None):
    if b is None:
        b = []
    pass

def foo(a, b: Optional[Sequence] = None):
    if b is None:
        b = []
    pass

if not users:
    print('no users')

if foo == 0:
    self.handle_zero()

if i % 10 == 0:
    self.handle_multiple_of_ten()

# Bad
def foo(a, b=[]):
    pass

def foo(a, b: Mapping = {}):
    pass

if len(users) == 0:  # foo != [] 등으로 체크하는 것도 비추, not users로 의미 전달 명확하게
    print('no users')

if foo is not None and not foo: # 0인 것을 암시적 False 대신 정수로 처리하는 것이 명확
    self.handle_zero()

if not i % 10: # 1 % 10 == 0과 같이 명시적으로 값을 비교하는 것이 좋다
    self.handle_multiple_of_ten()

```
