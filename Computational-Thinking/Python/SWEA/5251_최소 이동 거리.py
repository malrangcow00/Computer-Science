import sys
sys.stdin = open('input/5251.txt', 'r')
import heapq    # 이 문제는 다익스트라로 푸는거다 -> 최소힙을 갖다가 쓰자

# 편향트리의 형태의 그래프라고 가정
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())    # 1 <= V <= 1000,   1 <= w <= 10
    graph = [[float('inf')] * (V + 1) for i in range(V + 1)]     # 인접 행렬
    for _ in range(E):
        v1, v2, w = map(int, input().split())   # 1 <= v1, v2, w <= 1000
        graph[v1][v2] = w
    for i in range(V + 1):  # 출발지와 도착지가 같은 경우의 거리는 0 이다.
        graph[i][i] = 0

    res = [float('inf')] * (V + 1)   # 다익스트라 결과 배열 초기화
    res[0] = 0  # 0번 정점에서 시작
    heap = []   # 빈 힙
    heapq.heappush(heap, (0, 0))    # 힙에다가 (거리:0, 정점:0)을 넣자
    while heap:     # 힙이 비면 끝내자
        d, v = heapq.heappop(heap)  # 힙에서 하나 꺼내자
        for i in range(V + 1):  # 도착점
            if res[i] > d + graph[v][i]:    # 힙에서 꺼낸 정점을 거쳐가는 거리가 지금까지 생각한 최소거리보다 작으면
                res[i] = d + graph[v][i]    # 도착지점에 대한 최소거리를 갱신하자
                heapq.heappush(heap, (res[i], i))   # 갱신한 최소거리가 다른 최소거리를 결정하는데 영향을 줄 수 있게 힙에 넣자
    print(f'#{tc} {res[V]}')