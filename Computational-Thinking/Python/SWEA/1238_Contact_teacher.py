import sys
sys.stdin = open('input/1238.txt', 'r')

def BFS(start):
    queue = []
    queue.append(start)
    visited[start] = True

    # 같은 레벨(depth)의 노드들의 번호 중 가장 큰 값을 저장하는 변수
    mx = start
    while queue:
        qSize = len(queue)
        # 인접된 요소를 큐에다가 넣고 방문...
        for _ in range(qSize):
            node = queue.pop(0)
            for nxt in graphs[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
        # 아무런 노드가 없다 == 더 이상 방문할 노드가 없다.
        if len(queue) == 0:
            break
        mx = max(queue)  # 최대값 갱신
    return mx


for tc in range(1, 11):
    # 입력 받을 길이 N, 시작 노드 start
    N, start = map(int, input().split())

    # 간선 정보
    edges = list(map(int, input().split()))

    # 인접 리스트 저장...
    graphs = [[] for _ in range(101)]
    for idx in range(0, len(edges), 2):
        u = edges[idx]
        v = edges[idx + 1]
        graphs[u].append(v)  # u -> v

    # BFS 순회
    visited = [False] * 101
    answer = BFS(start)

    print(f"#{tc} {answer}")