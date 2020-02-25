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

#### heapq

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