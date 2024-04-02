import sys
sys.stdin = open('input/18418.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    mn = 1000

    for y in range(N):
        for x in range(N):
            tmp = arr[y][x]
            for i in range(4):
                for j in range(1, arr[y][x]+1):
                    nx = x + j*dx[i]
                    ny = y + j*dy[i]
                    if N > nx >= 0 and N > ny >= 0:
                        tmp += arr[ny][nx]
                    else:
                        break
            mx = max(mx, tmp)
            mn = min(mn, tmp)
    print(f'#{tc} {mx-mn}')