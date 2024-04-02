edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 정점의 개수
V = 7

# # 인접 행렬 : 이차원 배열에 저장...
# # u -> v : graph[u][v] = 1
# graph = [[0] * (V + 1) for _ in range(V + 1)]  # V x V 이차원 배열
# 
# # 한쌍의 정보 가져오기...
# for idx in range(0, len(edges), 2):
#     u = edges[idx]
#     v = edges[idx + 1]
# 
#     # 정점의 연결 정보를 인접 행렬에 저장...!
#     graph[u][v] = 1  # u -> v
#     graph[v][u] = 1  # v -> u (무향 그래프, 간선 저장)

# 인접 리스트 : 해당 정점 -> 인접한 정점들...
graph = [[] for _ in range(V + 1)]

# 한쌍의 정보 가져오기...
for idx in range(0, len(edges), 2):
    u = edges[idx]
    v = edges[idx + 1]

    # 정점의 연결 정보를 인접 리스트에 저장
    graph[u].append(v)  # u -> v
    graph[v].append(u)  # v -> u
    
# DFS 순회 (재귀 호출)
def DFS(current):
    visited[current] = True
    print(current, end=" -> ")
    for nxt in graph[current]:
        if not visited[nxt]:
            DFS(nxt)


visited = [False] * (V + 1) # 방문 체크
DFS(1) # 1번 정점에 대해서 DFS 시작...

# BFS 순회 (큐 자료구조)
def BFS(current):
    visited = [False] * (V + 1)
    queue = []
    queue.append(current)  # 큐에 시작 노드 추가
    visited[current] = True  # 시작 노드 방문 체크
    print()

    # 큐에 요소가 없을 때 까지 반복
    while queue:
        node = queue.pop(0)  # 큐에서 요소를 하나씩 꺼내면서 FIFO
        print(node, end=" -> ")
        # 인접한 노드들을 방문...
        for nxt in graph[node]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True


BFS(1)  # 1번 정점에 대해서 DFS 시작...
print()