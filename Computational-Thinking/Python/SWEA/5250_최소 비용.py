import sys
sys.stdin = open('input/5250.txt')
import heapq

# 입력처리 (그래프 : 인접 리스트)
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    # 양방향 그래프 (무향 그래프) # u -> v, v -> u
    graph[u].append((v, w))  # u -> v, 가중치 : w
    graph[v].append((u, w))  # v -> u, 가중치 : w

def dijkstra(graph, start):
    # dist: 시작정점 start ----> 각 정점에 대한 최단 거리의 비용을 저장하는 배열(DP)
    dist = [float('inf')] * V  # [float('inf') for _ in range(V)]
    dist[start] = 0
    # 우선순위큐.. 가장 최소 비용을 들고 있는 정점을 선택... (최소힙, 비용 낮은 값부터 pop!)
    min_heap = [(0, start)]

    while min_heap:
        cur_cost, node = heapq.heappop(min_heap)  # 가장 비용이 작은 정점..

        # 현재까지 계산했던 dist 경로의 최소값이 cur_cost 보다 작다면, 해당 노드는 skip!
        if cur_cost > dist[node]:
            continue

        # 인접한 노드들에 대해서 최소값을 dist에 갱신...!
        for nxt, w in graph[node]:
            new_cost = cur_cost + w
            if dist[nxt] > new_cost:  # 새로운
                dist[nxt] = new_cost
                heapq.heappush(min_heap, (new_cost, nxt))

    return dist

# 다익스트라 알고리즘 실행...
# 시작 정점 0
start = 0
shortest_dist = dijkstra(graph, start)
print(shortest_dist)  # 시작 정점 0 -> 해당 정점 i 에 대한 최소 경로 비용.









dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



def DFS(start):
    global mn
    global tmp
    if start == N**2-1:
        mn = min(mn, tmp)
        return
    else:
        for i in graph[start]:
            if not visited[i]:
                visited[i] = True
                cost = 1
                if arr[start//N][start%N] < arr[i//N][i%N]:
                    cost += (arr[i//N][i%N] - arr[start//N][start%N])
                visited[i] = True
                tmp += cost
                DFS(i)
                visited[i] = False
                tmp -= cost

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N*N)]
    mn = 0
    for y in range(N):
        for x in range(N):
            mn += arr[y][x]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    graph[x+N*y].append(nx+N*ny)
    visited = [False] * N**2
    visited[0] = True
    tmp = arr[0][0]
    DFS(0)
    print(f'#{tc} {mn}')