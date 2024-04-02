'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

def BFS(x, V):
    # 방문체크 배열
    visited = [False for _ in range(V + 1)]
    # 큐 자료구조
    q = []
    # 큐에 시작 정점을 넣고
    q.append(x)
    # 방문체크를 진행한다..
    visited[x] = True

    # 큐에 노드가 빌 때까지 탐색을 진행한다...
    while len(q) > 0:
        # 해당 정점을 큐에서 하나 뽑아서...
        x = q.pop(0)
        # 아직 방문하지 않은 인접 노드를 큐에 추가한다...
        for nxt in adj_l[x]:
            if visited[nxt] == False:
                q.append(nxt)
                visited[nxt] = True

BFS(1, 7)

V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
