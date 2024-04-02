import sys
sys.stdin = open('input/4875.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, visited):
    visited[y][x] = True
    for k in range(4):
        nx = x + dy[k]
        ny = y + dx[k]
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] in [0, 3] and visited[ny][nx] == False:
            dfs(nx, ny, visited)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                sy, sx = y, x
            elif arr[y][x] == 3:
                ey, ex = y, x
    visited = [[False] * N for _ in range(N)]

    dfs(sx, sy, visited)

    print(f'#{tc} ', end='')

    if visited[ey][ex] == True:
        print(1, end='')
    else:
        print(0, end='')
    print()
