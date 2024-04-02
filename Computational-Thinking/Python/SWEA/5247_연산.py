import sys
sys.stdin = open('input/5247.txt', 'r')

from collections import deque
def BFS(N):
    visited = [0]*1000001
    q = deque()
    q.append(N)

    while q:
        n = q.popleft()
        if n == M:
            return visited[n]
        for i in [n-1, n+1, 2*n, n-10]:
            if 1 <= i <= 1000000 and visited[i] == 0:
                visited[i] = visited[n] + 1
                q.append(i)

T = int(input())
for tc in range(1, T+1):
    # N -> M
    N, M = map(int, input().split())
    print(f'#{tc} {BFS(N)}')