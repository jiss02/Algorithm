# :pencil:Algorithm

<div align="center">
    알고리즘을 공부하고 저장해놓는 공간입니다.
</div>

> 사용언어: python

### 목차

---

- [특정 문자로 칸 채우기](#특정-문자로-칸-채우기)
- [비트연산자](#비트연산자)
- [heapq](#heapq)
- [collections](#collections)

---

### 익히면 좋을 함수 및 코드들

---

#### 특정 문자로 칸 채우기

1. zfill 함수
```python
    #"0002"
    "2".zfill(4)
```
2. rjust 함수
```python
    #00123
    "123".rjust(5,"0")
```
---

#### 비트연산자

파이썬은 기본적으로
```python
bin(), hex(), oct()
```
 함수를 제공한다.

| 연산자 | 기능 |
|:--|--:|
|&|비트간의 AND 연산|
|\||비트간의 OR 연산|
|^|비트간의 XOR 연산|
|~|비트간의 NOR 연산|
|<<|n번 비트를 왼쪽으로 이동시킴|
|>>|n번 비트를 오른쪽으로 이동시킴|

---

#### Heapq

`우선순위큐`를 위한 자료구조인 `힙`을 간편하게 사용하도록 도와주는 라이브러리이다.

1. 배열을 힙으로 만들기

```python
heapq.heapify(arrname)
```

2. `push` 및 `pop`

```
heapq.heappop(arrname)
heapq.heappush(arrname, num)
```

> max-heap은 지원하지않는다.

---

#### Collections

편리한 기능이 추가된 다양한 딕셔너리와 queue를 사용가능하게 해주는 라이브러리이다.

**종류**

- defaultdict : 딕셔너리 생성시, value의 디폴트 값을 설정해줄 수 있다.
- Oredereddict: value에 대해 **내림차순**으로 정렬해준다.
- Counter: 여러 중복 값이 존재하는 list를 넣어주면 각 요소가 몇개있는지 세어서 딕셔너리로 만들어준다. (오름차순으로 정렬까지 해준다!)
- deque: list를 queue처럼 사용가능하게 해준다. rotate(위치돌리기)와 leftpush, leftpop까지 제공한다.

