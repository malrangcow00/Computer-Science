import sys
sys.stdin = open('input/1238.txt', 'r')

def BFS(start):
    visited = [0] * 101 # 방문배열 생성
    q = [] # 큐 생성
    q.append(start) # 시작점 인큐
    visited[start] = 1 # 시작점 방문표시
    while q: # 큐에 정점이 남아있으면 front != rear
        p_num = q.pop(0) # 디큐
        for w in node[p_num]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[p_num] + 1
    print(f'#{tc}', 100 - visited[::-1].index(max(visited)))

for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 노드 생성
    node = [[] for _ in range(101)]

    # 노드 입력
    for _ in range(N//2):
        p1, p2 = arr[2*_], arr[2*_ + 1]
        node[p1].append(p2)

    BFS(start)