## Graph
- 코딩 테스트에 자주 출제되는 Graph 관련 문제들입니다.
- 어떤 유형이 있는지는 하나씩 정리해나가도록 하겠습니다.

## 1. DFS
-

## 2. BFS
- Breadth First Search, 너비 우선 탐색을 말한다.
- 그래프의 시작 노드에서부터 인접한 노드들을 순서대로 탐색한다.
- 말 그대로 너비를 우선시하는 탐색 알고리즘이다.
- BFS는 **모든 간선의 비용이 동일한 그래프에서 최단 경로**를 찾을 때 사용하면 된다. (핵심)
    - 경로 문제는 무조건 시작점과 도착점이 주어진다.
    - BFS 알고리즘의 동작 원리에 따라, 시작점부터 인접한 노드들을 너비 우선 순서대로 탐색한다.
    - 핵심은 그래프의 **모든 간선의 비용이 동일**하다는 것이다.
    - 너비 우선 탐색을 진행하다가 도착 노드가 발견된다면, 해당 경로가 최단 경로임이 보장된다. 모든 간선의 비용이 동일하기 때문이다.
    - 그래서 BFS를 활용한 최단 경로 탐색 문제를 풀 때, 최단 경로를 비교할 필요 없이 도착점에 도달하면 그 때까지의 거리를 반환하면 된다.
- [참고할만한 링크](https://heytech.tistory.com/56#)

## 3. 플로이드-워샬 알고리즘
-

## 4. 백트래킹
- 

## 5. 다익스트라 알고리즘
- 그래프 내의 출발 노드에서 도착 노드까지의 **최단 거리를 탐색하는 알고리즘**이다.
- 그래프는 노드(node)와 간선(edge)으로 이루어져 있으며, 각 간선마다 가중치(weight)가 부여될 수 있다.
- 그래프의 간선 중 **음의 가중치**를 갖는 간선이 있는 경우, 다익스트라 알고리즘을 **사용할 수 없다**.
- 다음은 다익스트라 알고리즘의 동작 원리이다.
    1. 입력으로 그래프가 주어진다. 다익스트라 알고리즘과 함께 주로 사용되는 그래프는 크게 **인접 리스트**, **인접 행렬**이 있다.
        ```python
        # 인접 리스트(Adjacency List)
        # 각 정점마다 해당 정점에 인접한 정점들과 가중치를 리스트, 딕셔너리 등으로 표현하는 방법.
        # 희소 그래프(Sparse Graph, 그래프에 필요없는 값이 많음)에 적합.
        # 메모리 효율적
        {
            'A': {'B': 2, 'C': 4},
            'B': {'A': 2, 'C': 1, 'D': 7},
            'C': {'A': 4, 'B': 1, 'D': 3},
            'D': {'B': 7, 'C': 3}
        }
        ```
        ```python
        # 인접 행렬(Adjacency Matrix)
        # 정점 간의 연결 관계를 이차원 배열로 표현
        # 밀집 그래프(Dense Graph, 그래프에 필요한 값들이 대부분인 경우), 간선의 수가 많은 경우 적합
               A   B   C   D
            A  0   2   4   ∞
            B  2   0   1   7
            C  4   1   0   3
            D  ∞   7   3   0
        ```
    2. 모든 정점까지의 거리(또는 가중치의 합)를 초기화한 배열을 선언한다. 이 때 배열의 값은 주로 무한대를 사용한다.
    3. 2번에서 선언한 배열 중 출발 노드의 거리는 0으로 초기화한다. 출발 노드부터 거리를 계산하기 때문이다.
    4. 우선순위 큐에 출발 노드의 정보를 저장한다.
    5. 우선순위 큐에서 노드를 가져온다.
    6. 가져온 노드의 인접 노드들의 정보를 가져와서, 누적 가중치를 계산한다. 계산한 누적 가중치는 출발 노드부터 인접 노드까지 가중치의 합을 의미한다.
    7. 계산한 누적 가중치와 거리 배열에 저장되어있는 누적 가중치를 비교한다. 전자가 후자보다 작을 경우,
    거리 배열을 새로 계산한 누적 가중치로 초기화하고 해당 노드의 정보를 큐에 추가한다.
    8. 큐가 빌 때까지 5 - 7 과정을 반복한다.
- 다익스트라 알고리즘의 코드 예시이다.
```python
def dijkstra(graph, start):
    dists = {node: float('inf') for node in graph.keys()} # 2
    dists[start] = 0 # 3

    queue = [(0, start)] # 4

    while queue: # 8
        # 5
        # 파이썬에서는 heapq 모듈로 min heap 자료구조를 이용하여 다익스트라를 구현한다.
        # min heap은 최소 값이 root node인 자료구조이다 -> 거리가 최소인 노드를 우선순위로 사용하는 큐라고 생각할 수 있다.
        curr_dist, curr_node = heapq.heappop(queue)

        # 과정을 반복하면서 큐에 동일한 노드에 대한 정보가 누적되는데, 불필요한 연산을 줄이기 위해 예외처리가 필요하다.
        if curr_dist > dists[curr_node]:
            continue

        for next_node, weight in graph[curr_node].items(): # 6
            dist = curr_dist + weight # 6

            if dist < dists[next_node]: # 7
                dists[next_node] = dist 
                heapq.heappush(queue, (dist, next_node))
```
- 다익스트라 알고리즘을 구현하는 방법에는 여러 가지가 있겠지만, heap 자료 구조를 이용한 구현이 일반적이다.
- `python`의 경우 `heapq`라는 내장 라이브러리를 이용하여 다익스트라 알고리즘을 구현한다.
- 다익스트라의 증명이 궁금하다면, [여기](https://gazelle-and-cs.tistory.com/91)를 참고하자. ~~읽다가 이해를 포기했다.~~

### 6. 최소 신장 트리(Minimum Spanning Tree)
- 크루스칼 알고리즘(Kruskal Algorithm)
- 프림 알고리즘(Prim Algorithm)


### 7. 위상 정렬(Topological Sorting)
- 그래프 정렬 알고리즘의 일종으로, 정점 간의 순서가 존재할 때 순서에 맞게 정점을 정렬하는 알고리즘이다.
- **순환이 없는 방향 그래프**일 때만 위상 정렬 적용이 가능하다.
- 위상 정렬을 위해선 진입 차수와 진출 차수에 대해 알아야 한다.
    - 진입 차수: 외부에서 하나의 정점으로 들어오는 간선의 수.
    - 진출 차수: 하나의 정점에서 외부로 나가는 간선의 수.
- 위상 정렬 알고리즘은 진입 차수를 이용한 BFS, 진출 차수를 이용한 DFS로 구현할 수 있다. 대부분 진입 차수를 이용한 BFS로 구현한다.
- 진입 차수를 이용한 위상 정렬은 다음과 같은 순서로 이루어진다.
    1. 모든 정점에 대해 진입 차수를 파악한다.
    2. 진입 차수가 0인 정점을 queue에 저장한다.
    3. Queue에서 정점을 하나씩 꺼내고, 꺼낸 결과를 저장한다.
    4. 꺼낸 정점과 연결되어 있는 정점들의 진입 차수를 수정한다.
    5. 진입 차수를 수정한 결과 0인 정점들을 다시 queue에 넣는다.
    6. queue가 빌 때까지 2-5 과정을 반복한다.
- Queue에서 꺼낸 순서가 위상 정렬된 순서이다.\
- 문제에서 **방향 그래프**, **순서** 와 같은 키워드가 보이는 경우 위상 정렬 문제일 확률이 매우 높다.
- [[여기]](https://m.terms.naver.com/entry.naver?docId=3579618&cid=59086&categoryId=59093)를 참고하면 조금 더 친절하게 설명한 글을 볼 수 있다.