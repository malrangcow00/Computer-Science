"""
# 첫줄 : 정점 개수(V), 간선 개수(E)
# 간선의 개수 E 줄에 대해서 (u -> v, 가중치 w)
7 11 
0 1 32 
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
# 입력 처리 (그래프: 인접 리스트)
# 정점 개수(V), 간선 개수(E)
V, E = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(V)]

# 간선 개수 E만큼 u -> v, 가중치 w를 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # 양방향 그래프 (무향 그래프), 불변형 자료형인 튜플로 저장하는 것을 권장
    graph[u].append((v, w))
    graph[v].append((u, w))
    





# Prim Algorithm (Greedy)
# 한 정점에 대해서 최소 가중치를 가진 
# 범위를 계속 확대하는 방식으로 진행
# 모든 노드(V)를 방문했을 때 중단 (V-1)개의 간선
import heapq

def prim(graph, start):
    # 방문 체크를 진행할 visited 배열 생성
    visited = [False] * V
    # 우선순위 큐: 최소힙(간선의 가중치가 낮은 값을 먼저 추출)
    # 첫 시작점과 그에 대한 가중치(cost) = 0, 가중치순 정렬을 위해 가중치를 먼저 추가
    min_heap = [(0, start)]
    MST = [] # 최소 신장 트리를 저장해서 반환할 리스트
    
    while min_heap:
        cost, node = heapq.heappop(min_heap) # 간선의 가중치 중 가장 작은 가중치를 가지고 있는 간선
        
        # 아직 방문하지 않은 정점이라면 방문
        if not visited[node]:
            visited[node] = True
            MST.append((node, cost))
            for nxt, cost in graph[node]:
                if not visited[nxt]:
                    # 연결된 정점을 최소 힙에 추가...
                    heapq.heappush(min_heap, (cost, nxt))
    
    return MST
# 출력: MST의 비용의 합을 출력
total_cost = 0
for node, cost in prim(graph, 0):
    total_cost += cost

# 출력: MST 비용의 합 출력
print('minimum cost by using prim algorithm :', total_cost)


# 크루스칼 알고리즘 (Greedy)
# 간선의 가중치를 기준으로 해서 모든
# 해당되는 가중치가 낮은 간선을 
# (단, 사이클이 발생하지 않는 간선

# 부모 노드를 찾는 함수 
def find(parents, x): 
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents, parents[x]) # 경로 압축
        return find(parents, parents[x])

def union(parents, x, y):
    # x, y에 대하나 부모 찾기...
    px = find(parents, x)
    py = find(parents, y)
    
    if px != py:
        parents[px] = py


def kruskal(graph):
    edges = [] # 모든 간선 정보가 있는 리스트
    for u in range(V):
        for v, w in graph[u]:
            edges.append((u, v, w)) # u -> v, 가중치 w
            
    # 간선 가중치를 기준으로 오름차순 정렬..
    edges.sort(key=lambda x: x[2])
    MST = [] # 최소 신장 트리를 반환할 리스트
    
    parents = [i for i in range(V)] # 각 정점의 부모를 초기화...
    
    for u, v, w in edges:
        if find(parents, u) != find(parents, v): # 이 간선을 추가한다면 사이클이 없는지 확인
            MST.append((u, v, w))
            union(parents, u, v) # 두 집합을 합치도록 진행
    return MST # 최소 신장 트리를 반환

# 출력: MST의 비용의 합을 출력
total_cost = 0
for u, v, w in kruskal(graph):
    total_cost += w
    
# 출력: MST 비용의 합 출력
print('minimum cost by using kruskal algorithm :', total_cost)