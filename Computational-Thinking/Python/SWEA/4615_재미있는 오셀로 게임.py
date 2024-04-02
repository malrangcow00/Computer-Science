import sys
sys.stdin = open('input/4615.txt', 'r')

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2 - 1][N//2], arr[N//2][N//2 - 1], arr[N//2 - 1][N//2 - 1] = 2, 1, 1, 2
    for _ in range(M):
        sx, sy, p = map(int, input().split())
        sx = sx - 1
        sy = sy - 1
        arr[sy][sx] = p
        for i in range(8):
            for j in range(1, N):
                nx = sx + j*dx[i]
                ny = sy + j*dy[i]
                if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == [1, 2][p % 2]:
                    continue
                elif 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == [1, 2][(p+1) % 2]:
                    while nx != sx or ny != sy:
                        nx -= dx[i]
                        ny -= dy[i]
                        arr[ny][nx] = [1, 2][(p+1) % 2]
                    break
                else:
                    break
    cnt_1 = 0
    cnt_2 = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                cnt_1 += 1
            elif arr[y][x] == 2:
                cnt_2 += 1
    print(f'#{tc} {cnt_1} {cnt_2}')


