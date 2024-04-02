import sys
# sys.stdin = open('input/1238.txt', 'r')
sys.stdin = open('input/test.txt', 'r')

def bfs(start):
    visited = [0] * 101 # 방문배열 생성
    q = [] # 큐 생성
    q.append(start) # 시작점 인큐
    visited[start] = 1 # 시작점 방문표시
    tmp = []
    cnt = 1
    while q: # 큐에 정점이 남아있으면 front != rear
        p_num = q.pop(0) # 디큐
        cnt -= 1
        if cnt == 1:
            tmp = []
        for contact in range(101): # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[contact] == 0 and node[p_num][contact] == 1:
                cnt += 1
                q.append(contact) # w인큐, 인큐되었음을 표시
                tmp.append(contact)
                visited[contact] = 1
    print(f'#{tc} {max(tmp)}')

# for tc in range(1, 11):
for tc in range(1, 2):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 노드 생성
    node = [[0] * 101 for _ in range(101)]

    # 노드 입력
    for _ in range(N//2):
        p1, p2 = arr[2*_], arr[2*_ + 1]
        node[p1][p2] = 1

    bfs(start)




