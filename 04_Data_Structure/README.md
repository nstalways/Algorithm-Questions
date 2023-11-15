## Data Structure
- 코딩 테스트에 자주 출제되는 자료 구조 관련 문제들입니다.
- **자료 구조 관련 문제를 풀 때 필요한 개념 및 Tip 들**을 README에 기록합니다.
1. 양방향 회전 큐는 `collections` 모듈의 `deque` 및 클래스 메소드인 `rotate()`를 사용하면 된다.
2. Python의 list 내부 값을 삭제할 때 이용할 수 있는 함수로는 `remove()`, `pop()`, `del`이 있다.
    - `remove()`: 지우고자 하는 값을 인자로 입력받는다. 동일한 값이 여러 개 존재하는 경우, 순서상 가장 앞에 존재하는 값을 제거한다. Inplace 연산이다.
    - `pop()`: 지우고자 하는 값의 위치를 인자로 입력받는다. 지우고자 하는 값을 반환하며, Inplace 연산이다.
    - `del`: 지우고자 하는 값으 위치를 인자로 입력받는다. 반환값은 없으며, Inplace 연산이다.
    - `del`이 `pop()`보다는 조금 더 빠르다. 반환값이 없기 때문이다.
    - Python의 연산에 대한 시간 복잡도가 궁금하다면 [여기](https://ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)를 참고해보자.

### 1. Heap
- [Reference](https://docs.python.org/ko/3/library/heapq.html)
- [Source](https://ko.wikipedia.org/wiki/%ED%9E%99_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))
- 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리(complete binary tree)를 기본으로 한 자료구조로서, 다음과 같은 힙 속성을 만족한다.
    - A가 B의 부모 노드이면, A의 키 값과 B의 키 값 사이에는 대소관계가 성립한다.
- 힙에는 두 가지 종류가 있으며, 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙을 **최대 힙**, 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙을 **최소 힙**이라고 부른다.
- 키 값의 대소 관계는 오로지 부모 노드와 자식 노드 간에만 성립하며, 특히 **형제 사이에는 대소 관계가 정해지지 않는다.**
- `Python`에서는 `heapq`라는 내장 모듈을 이용하면, heap 자료 구조를 쉽게 사용할 수 있다.
    ```python
    import heapq

    # 리스트를 사용하며, min heap이 default이다.
    pq = []

    # push
    heapq.heappush(pq, 1)
    
    # pop
    heapq.heappop(pq)

    # 리스트를 heap으로 변환
    heapq.heapify(tmp)

    # key를 적용해서 기준에 부합하는 n개의 노드를 반환
    heapq.nlargest(n, iterable, key=None)
    heapq.nsmallest(n, iterable, key=None)
    ```
- 만약 max heap을 구현하고 싶다면, push할 때 음수 부호를 달아 반전하는 방식으로 쉽게 구현이 가능하다.
- 만약 최소 혹은 최대 값이 중복되는 경우, 다음 값을 비교하여 최소 혹은 최대 값을 결정한다.
    ```python
    import heapq

    pq = []

    heapq.heappush(pq, (1, 1))
    heapq.heappush(pq, (1, -1))

    heapq.heappop(pq)
    >>> (1, -1)
    ```
- `heapq`에서 구현한 heap은 모든 k에 대해 `heap[k] <= heap[2*k + 1]`과 `heap[k] <= heap[2*k + 2]`를 만족한다. 즉 부모 노드와 자식 노드 간의 대소 관계는 위 조건에 따라 구현되어있다.
    ```python
    import heapq

    pq = []

    for i in range(1, 6):
        heapq.heappush(pq, i)

    pq
    >>> [1, 2, 3, 4, 5]
    ```
    - k=0일 때) `pq[0] <= pq[2*0 + 1], pq[2*0 + 2]`를 만족한다.
    - k=1일 때) `pq[1] <= pq[2*1 + 1], pq[2*1 + 2]`를 만족한다.
- 정리하자면, **heap 자료 구조는 최소 혹은 최대 값을 빠르게 찾기 위해 고안된 완전이진트리의 일종이며, 부모 노드와 자식 노드 간의 대소 관계만 성립하고, 자식 노드 간의 대소 관계는 성립하지 않는다.**
